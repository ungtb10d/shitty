/*
 * rewrap.h
 * Copyright (C) 2016 Kovid Goyal <kovid at ungtb10d.net>
 *
 * Distributed under terms of the GPL3 license.
 */

#pragma once

#ifndef BufType
#define BufType LineBuf
#endif

#ifndef init_src_line
#define init_src_line(src_y) linebuf_init_line(src, src_y);
#endif

#define set_dest_line_attrs(dest_y, continued_) dest->line_attrs[dest_y] = src->line->attrs; if (continued_) dest->line_attrs[dest_y].continued = true; src->line->attrs.prompt_kind = UNKNOWN_PROMPT_KIND;

#ifndef first_dest_line
#define first_dest_line linebuf_init_line(dest, 0); set_dest_line_attrs(0, false)
#endif

#ifndef next_dest_line
#define next_dest_line(continued) \
    if (dest_y >= dest->ynum - 1) { \
        linebuf_index(dest, 0, dest->ynum - 1); \
        if (historybuf != NULL) { \
            linebuf_init_line(dest, dest->ynum - 1); \
            dest->line->attrs.has_dirty_text = true; \
            historybuf_add_line(historybuf, dest->line, as_ansi_buf); \
        }\
        linebuf_clear_line(dest, dest->ynum - 1, true); \
    } else dest_y++; \
    linebuf_init_line(dest, dest_y); \
    set_dest_line_attrs(dest_y, continued);
#endif

#ifndef is_src_line_continued
#define is_src_line_continued(src_y) (src_y + 1 < src->ynum ? (src->line_attrs[src_y + 1].continued) : false)
#endif

static inline void
copy_range(Line *src, index_type src_at, Line* dest, index_type dest_at, index_type num) {
    memcpy(dest->cpu_cells + dest_at, src->cpu_cells + src_at, num * sizeof(CPUCell));
    memcpy(dest->gpu_cells + dest_at, src->gpu_cells + src_at, num * sizeof(GPUCell));
}

typedef struct TrackCursor {
    index_type x, y;
    bool is_tracked_line, is_sentinel;
} TrackCursor;


static void
rewrap_inner(BufType *src, BufType *dest, const index_type src_limit, HistoryBuf UNUSED *historybuf, TrackCursor *track, ANSIBuf *as_ansi_buf) {
    bool src_line_is_continued = false, is_first_line = true;
    index_type src_y = 0, src_x = 0, dest_x = 0, dest_y = 0, num = 0, src_x_limit = 0;
    TrackCursor tc_end = {.is_sentinel = true };
    if (!track) track = &tc_end;

    do {
        for (TrackCursor *t = track; !t->is_sentinel; t++) t->is_tracked_line = src_y == t->y;
        init_src_line(src_y);
        src_line_is_continued = is_src_line_continued(src_y);
        src_x_limit = src->xnum;
        if (!src_line_is_continued) {
            // Trim trailing blanks since there is a hard line break at the end of this line
            while(src_x_limit && (src->line->cpu_cells[src_x_limit - 1].ch) == BLANK_CHAR) src_x_limit--;
        }
        for (TrackCursor *t = track; !t->is_sentinel; t++) {
            if (t->is_tracked_line && t->x >= src_x_limit) t->x = MAX(1u, src_x_limit) - 1;
        }
        if (is_first_line) {
            first_dest_line; is_first_line = false;
        }
        while (src_x < src_x_limit) {
            if (dest_x >= dest->xnum) { next_dest_line(true); dest_x = 0; }
            num = MIN(src->line->xnum - src_x, dest->xnum - dest_x);
            copy_range(src->line, src_x, dest->line, dest_x, num);
            for (TrackCursor *t = track; !t->is_sentinel; t++) {
                if (t->is_tracked_line && src_x <= t->x && t->x < src_x + num) {
                    t->y = dest_y;
                    t->x = dest_x + (t->x - src_x + (t->x > 0));
                }
            }
            src_x += num; dest_x += num;
        }
        src_y++; src_x = 0;
        if (!src_line_is_continued && src_y < src_limit) { init_src_line(src_y); next_dest_line(false); dest_x = 0; }
    } while (src_y < src_limit);
    dest->line->ynum = dest_y;
}

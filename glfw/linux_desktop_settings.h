/*
 * Copyright (C) 2021 ungtb10d <kovid at ungtb10d.net>
 *
 * Distributed under terms of the GPL3 license.
 */

#pragma once

#include "dbus_glfw.h"
#include "internal.h"


void glfw_initialize_desktop_settings(void);
void glfw_current_cursor_theme(const char **theme, int *size);

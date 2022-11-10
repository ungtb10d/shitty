/*
 * Copyright (C) 2021 ungtb10d <kovid at ungtb10d.net>
 *
 * Distributed under terms of the GPL3 license.
 */

#pragma once
#include <wayland-client.h>

#define GLFW_WAYLAND_TEXT_INPUT_INTERFACE_NAME "zwp_text_input_manager_v3"

void _glfwWaylandBindTextInput(struct wl_registry* registry, uint32_t name);
void _glfwWaylandInitTextInput(void);
void _glfwWaylandDestroyTextInput(void);

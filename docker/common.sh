#!/usr/bin/env bash
#
# Shared helpers for the build scripts in this directory.
# Sourced, not executed.

# Pick a container engine. Honor $ENGINE if set; otherwise prefer
# `docker` (which may itself be a `podman`-compatible CLI), then `podman`.
detect_engine() {
	if [[ -n ${ENGINE:-} ]]; then
		printf '%s\n' "$ENGINE"
		return
	fi
	if command -v docker >/dev/null 2>&1; then
		printf 'docker\n'
	elif command -v podman >/dev/null 2>&1; then
		printf 'podman\n'
	else
		echo "Neither 'docker' nor 'podman' found in PATH." >&2
		exit 1
	fi
}

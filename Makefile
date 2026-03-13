SHELL := /usr/bin/env bash
.DEFAULT_GOAL := help

MAKEFLAGS += --no-builtin-rules

ROOT_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME ?= Block-Bricks
VENV_DIR ?= $(ROOT_DIR)/.venv
PYTHON ?= $(VENV_DIR)/bin/python
PIP ?= $(VENV_DIR)/bin/pip
SYSTEM_PYTHON ?= python3
APP_ENTRY ?= $(ROOT_DIR)/main.py
RUNTIME_DIR ?= $(ROOT_DIR)/.local/runtime
PID_FILE ?= $(RUNTIME_DIR)/block-bricks.pid
LOG_FILE ?= $(RUNTIME_DIR)/block-bricks.log
TAIL_LINES ?= 50

export ROOT_DIR PROJECT_NAME VENV_DIR PYTHON PIP SYSTEM_PYTHON APP_ENTRY RUNTIME_DIR PID_FILE LOG_FILE TAIL_LINES

include make/common.mk
include make/python.mk
include make/quality.mk
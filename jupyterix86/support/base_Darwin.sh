#!/bin/sh

SRCFILE="$1"
TARGET="$2"

as ${SRCFILE} -o /tmp/${TARGET}.o
ld -lc -macosx_version_min 10.13 /tmp/${TARGET}.o -o /tmp/${TARGET}.run
/tmp/${TARGET}.run
rm /tmp/${TARGET}.run
rm /tmp/${TARGET}.o

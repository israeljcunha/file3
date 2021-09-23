#!/usr/bin/env bash
cc_types="feat fix"
default_types="build ci docs $cc_types perf refactor revert test hotfix bugfix merge"
types=( $cc_types )

if [ $# -eq 1 ]; then
    types=( $default_types )
else
    while [ $# -gt 1 ]; do
        types+=( $1 )
        shift
    done
fi

msg_file=$1

r_types="($(IFS='|'; echo "${types[*]}"))"
r_scope="(\([\w \/-]+\))?"
r_delim='!?:'
r_subject=" [\w][\s\S]+"
pattern="^$r_types$r_scope$r_delim$r_subject$"

if ! grep -Pq "$pattern" "$msg_file"; then
    echo "[Commit message] $( cat $msg_file )"
    echo "
Your commit message does not follow Conventional Commits formatting
https://www.conventionalcommits.org/

Conventional Commits start with one of the below types, followed by a colon,types
followed by the commit message:

    $(IFS=' '; echo "${types[*]}")

Example commit message adding a feature:

    feat: implement new API

Example commit message fixing an issue:

    hotfix: remove infinite loop

Optionally, include a scope in parentheses after the type for more context:

    fix(account): remove infinite loop
"
    exit 1
fi

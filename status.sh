#!/bin/bash

pushd () {
    command pushd "$@" > /dev/null
}
popd () {
    command popd "$@" > /dev/null
}

cd ..
for dir in `ls`
  do pushd $dir
  status=
  if [[ ! -z $(git status --short) ]] ; then
    echo $dir
    git status
  fi
  popd
done

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
  git remote update > /dev/null
  if [[ ! -z $(git status --short) ]] ; then
    echo $dir
    git status
  else
    git push --quiet
  fi
  popd
done

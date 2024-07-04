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
  # echo $dir
  git remote update > /dev/null
  if [[ ! -z $(git status --short) ]] ; then
    echo $dir
    git status --short
  else
    git pull --quiet
    git push --quiet
  fi
  popd
done

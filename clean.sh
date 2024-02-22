#!/bin/bash

for file in `ls ../Relex12.github.io/*.md | grep -v README`
  do rm $file
done

for file in `ls ../Relex12.github.io/*.html | grep -v 404`
  do rm $file
done

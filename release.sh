#!/bin/bash

if [[ -z $1 ]]; then
  echo "Usage: ./release <VERSION>"
  exit 1
fi

version=$1

git push origin develop
git checkout master
git merge develop
git push origin master
git tag -a $version -m "Release $version"
git push origin $version

./build.sh
docker tag znibb/wplt:latest znibb/wplt:$version
docker push znibb/wplt:$version
docker push znibb/wplt:latest

exit 0

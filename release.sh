#!/bin/bash

version=$1
current_branch=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD)
user=znibb
name=wplt

# Check that script was run with argument
if [[ -z $1 ]]; then
  echo "Usage: ./release <VERSION>"
  exit 1
# Check that script was run from the intended branch
elif [[ $current_branch != "develop" ]]; then
  echo "Must be used from develop branch"
  exit 2
fi

# Update displayed version number on web page
sed -i "s/VERSION=\".*\"/VERSION=\"$version\"/" app/routes.py
git add app/routes.py
git commit -m "Updated displayed version number to $version"

# Push updates and merge with master
git push origin develop
git checkout master
git merge develop
git push origin master

# Create and push tag for new version
git tag -a $version -m "Release $version"
git push origin $version

# Return to development branch
git checkout develop
git merge master
git push origin develop

# Build and push new docker images
./build.sh
docker tag $user/$name:latest $user/$name:$version
docker push $user/$name:$version
docker push $user/$name:latest

# Exit gracefully
exit 0

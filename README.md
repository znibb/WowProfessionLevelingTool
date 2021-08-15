# WowProfessionLevelingTool

Do yu dislike the randomness of Wowhead profession guides? Then this is the tool for you!

This version is for World of Warcraft The Burning Crusade Classic.

## Local development
1. Install python3
1. Install python3-pip
1. Clone git repo: `git clone https://github.com/znibb/WowProfessionLevelingTool`
1. Enter repo directory: `cd WowProfessionLevelingTool`
1. Run startup script: `./runDevelopment.sh`

## Pull profession database updates
1. git submodule update --remote

## Deployment
1. Install docker
1. Install docker-compose
1. Download docker-compose.yml: `wget https://raw.githubusercontent.com/znibb/WowProfessionLevelingTool/master/docker-compose.yml`
1. Deploy: `docker-compose up -d`

## Changelog
### 2.0.0
#### Features added
- Initial version for BCC!

### 2.0.1
#### Bug fixes
- Fixed itemID for Ring of Silver Might

[//]: # (#### Features added)
[//]: # ()
[//]: # (#### Bug fixes)

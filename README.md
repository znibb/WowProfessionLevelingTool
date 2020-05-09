# WowProfessionLevelingTool

Want to know how to level a profession as cheap as possible? Then this is the tool for you!

## Local development
1. Install python3
1. Install python3-pip
1. Clone git repo: `git clone https://github.com/znibb/WowProfessionLevelingTool`
1. Enter repo directory: `cd WowProfessionLevelingTool`
1. Run startup script: `./runDevelopment.sh`

## Deployment
1. Install docker
1. Install docker-compose
1. Download docker-compose.yml: `wget https://raw.githubusercontent.com/znibb/WowProfessionLevelingTool/master/docker-compose.yml`
1. Deploy: `docker-compose up -d`

## Changelog
### 1.1.0
#### Features added
- Added cooking

#### Bug fixes
- Added missing server US-Azshara
- Fixed server names containing spaces from causing errors

### 1.0.1
- Removed vendor-back-gold from being calculated from enchanting
- Fixed formatting error in leatherworking recipe list
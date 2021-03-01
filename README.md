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

## ToDo
- Add engineering tools in the same way as enchanting rods

### 1.6.0
#### Features added
- Added ability to select desired difficulty limiter

## Changelog
### 1.5.4
#### Bug fixes
- Fixed a potential error when a reagent hasn't been seen on the AH and thus have no determinable price.

### 1.5.3
#### Bug fixes
- Fixed source for Runecloth Cloak
- Fixed skill level for Minor Rejuvanation Potion

### 1.5.2
#### Bug fixes
- Actually fixed watchtower settings
- Style updates to release.sh

### 1.5.1
#### Bug fixes
- Removed docker socket read-only flag for watchtower in docker-compose.yml
- Fetched minor cleanup updates from database submodule

### 1.5.0
#### Features added
- Updated available recipes for phase 5
- Moved profession database to separate repository and included as git submodule instead

#### Bug fixes
- Fixed typo in Enchant Bracer - Greater Stamina

### 1.4.0
#### Features added
- Added separate listing of recipes from different sources
- Added tooltips for recipes
- Added message to the user if it's not possible to reach the desired skill level
- Now retrieves server list from Nexushub instead of being hardcoded
- Price data is now retrieved in one big chunk instead of through one request per item! This speeds up handling the user request by a factor of 2 but comes at the cost of the information about the oldest data used (due to limitations in what data Nexushub returns)
- Added option to use the skillup from crafting Enchanting rods into the calculation

#### Bug fixes
- Grammar updates in user instructions
- Fixed an issue with image sizes for Firefox

### 1.3.1
#### Bug fixes
- Added conditional treatment of tooltips for enchanting crafts (use 'spell' instead of 'item' in wowhead url)
- Fixed minor typos in database

### 1.3.0
#### Features added
- Now also lists what recipes will need to be purchased from vendor
- Added some simple bootstrap styling
- Added graphical makeover
- Added wowhead tooltips to reagents and crafted items.

#### Bug fixes
- Fixed some errors with schools for blacksmithing recipes

### 1.2.0
#### Features added
- Now takes Leatherworking schools into consideration
- Now takes into account that some crafts create multiples of an item (e.g. grenades)

#### Bug fixes
- Removed Mooncloth recipe due to having long cooldown

### 1.1.0
#### Features added
- Added Cooking profession

#### Bug fixes
- Added missing server US-Azshara
- Fixed server names containing spaces from causing errors

### 1.0.1
- Removed vendor-back-gold from being calculated from enchanting
- Fixed formatting error in leatherworking recipe list

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
### 1.4.0
#### Features added
- Added separate listing of recipes from different sources
- Added tooltips for recipes
- Added message to the user if it's not possible to reach the desired skill level
- Now retrieves server list from Nexushub instead of being hardcoded

#### Bug fixes
- Grammar updates in user instructions
- Fixed an issue with image sizes for Firefox (kudos to [TheDonUK](https://github.com/TheDonUK))

### 1.3.1
#### Bug fixes
- Added conditional treatment of tooltips for enchanting crafts (use 'spell' instead of 'item' in wowhead url)
- Fixed minor typos in database

### 1.3.0
#### Features added
- Now also lists what recipes will need to be purchased from vendor
- Added some simple bootstrap styling (kudos to [miotke](https://github.com/miotke))
- Added graphical makeover (kudos to [TheDonUK](https://github.com/TheDonUK))
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

### ToDo
- Implement "slug fetch" of reagent price data" (https://api.nexushub.co/wow-classic/v1/items/noggenfogger-horde/)
- Enchanting note about disenchanting to lvl 40
- Enchanting, check lesser vs greater essences
- Enchanting rods
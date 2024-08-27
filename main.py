import cloudscraper

Scraper = cloudscraper.create_scraper()

def has_game(gamemode: str, auth: str):
    if gamemode == "mines":
        r1 = Scraper.get('https://api.bloxflip.com/games/mines', headers={"x-auth-token": auth}, params={"size": '1', "page": '0'})
        return r1.json()['hasGame']
    elif gamemode == "towers":
        r1 = Scraper.get('https://api.bloxflip.com/games/towers', headers={"x-auth-token": auth}, params={"size": '1', "page": '0'})
        return r1.json()['hasGame']

def get_game_data(gamemode: str, auth: str, size: int):
    if gamemode == "mines":
        r1 = Scraper.get('https://api.bloxflip.com/games/mines/history', headers={"x-auth-token": auth}, params={"size": size, "page": '0'})
        return r1.json()['data']
    elif gamemode == "towers":
        r1 = Scraper.get('https://api.bloxflip.com/games/towers/history', headers={"x-auth-token": auth}, params={"size": size, "page": '0'})
        return r1.json()['data']

def pastgames(gamemode: str, auth: str, click_emoji: str, bomb_emoji: str):
    if gamemode == "mines":

        # hasGame Testing is off!
        #test = has_game(gamemode, auth)
        #if not test:
        #    print("No Active Game!")
        #    return
        
        data = get_game_data(gamemode, auth, 100)
        if not data:
            print("No Game Data Found!")
            return
        latest_game = data[99]
        mine_locations = latest_game['mineLocations']

        grid_size = 5
        grid = [[bomb_emoji] * grid_size for _ in range(grid_size)]

        for mine in mine_locations:
            row = mine // grid_size
            col = mine % grid_size
            grid[row][col] = click_emoji

        for row in grid:
            print(' '.join(row))
            return

    elif gamemode == "towers":

        # hasGame Testing is off!
        #test = has_game(gamemode, auth)
        #if not test:
        #    print("No Active Game!")
        #    return

        data = get_game_data(gamemode, auth, 100)
        if not data:
            print("No Game Data Found!")
            return

        latest_game = data[99]
        tower_levels = latest_game['towerLevels']

        for level in tower_levels:
            row = [click_emoji if cell == 1 else bomb_emoji for cell in level]
            print(' '.join(row))
	    return

auth_token = ''   #put ur bloxflip token here
pastgames('mines', auth_token, "⭐️", "❌")
pastgames('towers', auth_token, "⭐️", "❌")

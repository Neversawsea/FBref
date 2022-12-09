import ScraperFC as sfc
import traceback
import pandas as pd

def gk():
    scraper = sfc.FBRef()
    df = pd.DataFrame()
    try:
        out = scraper.scrape_gk(2022, 'EPL', normalize=True, player=True)
    except:
        traceback.print_exc()
        scraper.close()
    df = out
    return df

def adv_gk():
    scraper = sfc.FBRef()
    df = pd.DataFrame()
    try:
        out = scraper.scrape_adv_gk(2022, 'EPL', normalize=True, player=True)
    except:
        traceback.print_exc()
        scraper.close()
    df = out
    return df

def shooting():
    scraper = sfc.FBRef()
    df = pd.DataFrame()
    try:
        out = scraper.scrape_shooting(2022, 'EPL', normalize=True, player=True)
    except:
        traceback.print_exc()
        scraper.close()
    df = out
    return df

def passing():
    scraper = sfc.FBRef()
    df = pd.DataFrame()
    try:
        out = scraper.scrape_passing(2022, 'EPL', normalize=True, player=True)
    except:
        traceback.print_exc()
        scraper.close()
    df = out
    return df

def goal_shot_creation():
    scraper = sfc.FBRef()
    df = pd.DataFrame()
    try:
        out = scraper.scrape_goal_shot_creation(2022, 'EPL', normalize=True, player=True)
    except:
        traceback.print_exc()
        scraper.close()
    df = out
    return df

def defensive():
    scraper = sfc.FBRef()
    df = pd.DataFrame()
    try:
        out = scraper.scrape_defensive(2022, 'EPL', normalize=True, player=True)
    except:
        traceback.print_exc()
        scraper.close()
    df = out
    return df

def possession():
    scraper = sfc.FBRef()
    df = pd.DataFrame()
    try:
        out = scraper.scrape_possession(2022, 'EPL', normalize=True, player=True)
    except:
        traceback.print_exc()
        scraper.close()
    df = out
    return df

def passing_types():
    scraper = sfc.FBRef()
    df = pd.DataFrame()
    try:
        out = scraper.scrape_passing_types(2022, 'EPL', normalize=True, player=True)
    except:
        traceback.print_exc()
        scraper.close()
    df = out
    return df

def league():
    scraper = sfc.FBRef()
    df = pd.DataFrame()
    try:
        out = scraper.scrape_league_table(2022, 'EPL')
    except:
        traceback.print_exc()
        scraper.close()
    df = out
    return df

def game_stats():
    scraper = sfc.Understat()
    df = pd.DataFrame()
    try:
        out = scraper.scrape_game_states(2022, 'EPL')
    except:
        traceback.print_exc()
        scraper.close()
    df = out
    return df

def report():
    shooting = shooting()
    


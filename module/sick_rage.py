import helper_functions as hf
import os

def install(sick_user, sick_pass, download_dir, rename_dir, trakt_user, torrent_user, torrent_pass):
    os.system("sudo apt-get --yes --force-yes install p7zip-full")
    os.system("wget http://sourceforge.net/projects/bananapi/files/unrar_5.2.6-1_armhf.deb")
    os.system("sudo dpkg -i unrar_5.2.6-1_armhf.deb")
    os.system("rm  unrar_5.2.6-1_armhf.deb")
    os.system("sudo useradd sickrage")
    os.system("sudo usermod -a -G osmc sickrage")
    os.system("sudo git clone https://github.com/SiCKRAGE/SickRage.git /opt/sickrage")
    os.system("sudo cp /opt/sickrage/runscripts/init.systemd /etc/systemd/system/sickrage.service")
    os.system("sudo chown -R sickrage:sickrage /opt/sickrage")
    os.system("sudo chmod +x /opt/sickrage")
    os.system("sudo chmod a-x /etc/systemd/system/sickrage.service")
    # os.system("cd /etc/systemd/system")
    os.system("sudo mv /etc/systemd/system/sickrage.service .")
    os.system("sudo sed -i 's@/usr/bin/python2.7 /opt/sickrage/SickBeard.py -q --daemon --nolaunch --datadir=/opt/sickrage@/opt/sickrage/SickBeard.py -q --daemon --nolaunch --datadir=/opt/sickrage@g' sickrage.service")
    os.system("sudo mv sickrage.service /etc/systemd/system/sickrage.service")
    os.system("sudo systemctl enable sickrage.service")
    os.system("sudo systemctl start sickrage.service")
    os.system("sudo service sickrage stop")
    os.system("sudo mv /opt/sickrage/config.ini .")
    os.system("""sudo sed -i 's@web_username = ""@web_username = """+'"'+sick_user+'"'+"""@g' config.ini""")
    os.system("""sudo sed -i 's@web_password = ""@web_password = """+'"'+sick_pass+'"'+"""@g' config.ini""")
    os.system("sudo mv conig.ini /opt/sickrage/config.ini")
    # with open("tmp_sickrage", 'w+') as new_file:
    #     new_file.write(gen_config_file(sick_user, sick_pass, download_dir, rename_dir, trakt_user, torrent_pass))
    # os.system("sudo mv tmp_sickrage /opt/sickrage/config.ini")
    os.system("sudo service sickrage start")
    return """
    ----- SiCKRAGE:
        user: """+sick_user+"""
        pass: """+sick_pass+"""
        port: 8081
    """
def gen_config_file(user, password, download_dir, rename_dir, trakt_user, torrent_user, torrent_pass):
    return """
    [HORRIBLESUBS]
    horriblesubs = 1
    horriblesubs_ratio = ""
    horriblesubs_minseed = 1
    horriblesubs_minleech = 0
    horriblesubs_search_mode = eponly
    horriblesubs_search_fallback = 0
    horriblesubs_enable_daily = 1
    horriblesubs_enable_backlog = 1
    horriblesubs_cookies = ""
    [SKYTORRENTS]
    skytorrents = 1
    skytorrents_custom_url = ""
    skytorrents_ratio = ""
    skytorrents_minseed = 1
    skytorrents_minleech = 0
    skytorrents_search_mode = eponly
    skytorrents_search_fallback = 0
    skytorrents_enable_daily = 1
    skytorrents_enable_backlog = 1
    skytorrents_cookies = ""
    [HOUNDDAWGS]
    hounddawgs = 1
    hounddawgs_username = ""
    hounddawgs_password = ""
    hounddawgs_ranked = 1
    hounddawgs_ratio = ""
    hounddawgs_minseed = 1
    hounddawgs_minleech = 0
    hounddawgs_freeleech = 0
    hounddawgs_search_mode = eponly
    hounddawgs_search_fallback = 0
    hounddawgs_enable_daily = 1
    hounddawgs_enable_backlog = 1
    hounddawgs_cookies = ""
    [HDBITS]
    hdbits = 1
    hdbits_username = ""
    hdbits_passkey = ""
    hdbits_ratio = ""
    hdbits_search_mode = eponly
    hdbits_search_fallback = 0
    hdbits_enable_daily = 1
    hdbits_enable_backlog = 1
    hdbits_cookies = ""
    [ABNORMAL]
    abnormal = 1
    abnormal_username = ""
    abnormal_password = ""
    abnormal_ratio = ""
    abnormal_minseed = 1
    abnormal_minleech = 0
    abnormal_search_mode = eponly
    abnormal_search_fallback = 0
    abnormal_enable_daily = 1
    abnormal_enable_backlog = 1
    abnormal_cookies = ""
    [ALPHARATIO]
    alpharatio = 0
    alpharatio_username = ""
    alpharatio_password = ""
    alpharatio_ratio = ""
    alpharatio_minseed = 1
    alpharatio_minleech = 0
    alpharatio_search_mode = eponly
    alpharatio_search_fallback = 0
    alpharatio_enable_daily = 1
    alpharatio_enable_backlog = 1
    alpharatio_cookies = ""
    [SCENETIME]
    scenetime = 0
    scenetime_username = ""
    scenetime_password = ""
    scenetime_ratio = ""
    scenetime_minseed = 1
    scenetime_minleech = 0
    scenetime_search_mode = eponly
    scenetime_search_fallback = 0
    scenetime_enable_daily = 1
    scenetime_enable_backlog = 1
    scenetime_cookies = ""
    [GFTRACKER]
    gftracker = 0
    gftracker_username = ""
    gftracker_password = ""
    gftracker_ratio = ""
    gftracker_minseed = 1
    gftracker_minleech = 0
    gftracker_search_mode = eponly
    gftracker_search_fallback = 0
    gftracker_enable_daily = 1
    gftracker_enable_backlog = 1
    gftracker_cookies = ""
    [RARBG]
    rarbg = 1
    rarbg_ranked = 1
    rarbg_sorting = seeders
    rarbg_ratio = ""
    rarbg_minseed = 1
    rarbg_minleech = 0
    rarbg_search_mode = eponly
    rarbg_search_fallback = 0
    rarbg_enable_daily = 1
    rarbg_enable_backlog = 1
    rarbg_cookies = ""
    [HDSPACE]
    hdspace = 0
    hdspace_username = ""
    hdspace_password = ""
    hdspace_ratio = ""
    hdspace_minseed = 1
    hdspace_minleech = 0
    hdspace_search_mode = eponly
    hdspace_search_fallback = 0
    hdspace_enable_daily = 1
    hdspace_enable_backlog = 1
    hdspace_cookies = ""
    [BTN]
    btn = 0
    btn_api_key = ""
    btn_ratio = ""
    btn_search_mode = eponly
    btn_search_fallback = 0
    btn_enable_daily = 1
    btn_enable_backlog = 1
    btn_cookies = ""
    [TORRENTZ]
    torrentz = 1
    torrentz_ratio = ""
    torrentz_minseed = 1
    torrentz_minleech = 0
    torrentz_search_mode = eponly
    torrentz_search_fallback = 0
    torrentz_enable_daily = 1
    torrentz_enable_backlog = 1
    torrentz_cookies = ""
    [ELITETORRENT]
    elitetorrent = 0
    elitetorrent_onlyspasearch = 0
    elitetorrent_ratio = ""
    elitetorrent_minseed = 1
    elitetorrent_minleech = 0
    elitetorrent_search_mode = eponly
    elitetorrent_search_fallback = 0
    elitetorrent_enable_daily = 1
    elitetorrent_enable_backlog = 1
    elitetorrent_cookies = ""
    [CPASBIEN]
    cpasbien = 0
    cpasbien_ratio = ""
    cpasbien_minseed = 1
    cpasbien_minleech = 0
    cpasbien_search_mode = eponly
    cpasbien_search_fallback = 0
    cpasbien_enable_daily = 0
    cpasbien_enable_backlog = 1
    cpasbien_cookies = ""
    [TNTVILLAGE]
    tntvillage = 0
    tntvillage_username = ""
    tntvillage_password = ""
    tntvillage_engrelease = 0
    tntvillage_ratio = ""
    tntvillage_minseed = 1
    tntvillage_minleech = 0
    tntvillage_search_mode = eponly
    tntvillage_search_fallback = 0
    tntvillage_enable_daily = 1
    tntvillage_enable_backlog = 1
    tntvillage_cat = 0
    tntvillage_subtitle = 0
    tntvillage_cookies = ""
    [XTHOR]
    xthor = 0
    xthor_api_key = ""
    xthor_ratio = ""
    xthor_freeleech = 0
    xthor_search_mode = eponly
    xthor_search_fallback = 0
    xthor_enable_daily = 1
    xthor_enable_backlog = 1
    xthor_cookies = ""
    [SHAZBAT_TV]
    shazbat_tv = 0
    shazbat_tv_passkey = ""
    shazbat_tv_ratio = ""
    shazbat_tv_options = ""
    shazbat_tv_search_mode = eponly
    shazbat_tv_search_fallback = 0
    shazbat_tv_enable_daily = 1
    shazbat_tv_enable_backlog = 0
    shazbat_tv_cookies = ""
    [TORRENTPROJECT]
    torrentproject = 0
    torrentproject_custom_url = ""
    torrentproject_ratio = ""
    torrentproject_minseed = 1
    torrentproject_minleech = 0
    torrentproject_search_mode = eponly
    torrentproject_search_fallback = 0
    torrentproject_enable_daily = 0
    torrentproject_enable_backlog = 1
    torrentproject_cookies = ""
    [TORRENTBYTES]
    torrentbytes = 0
    torrentbytes_username = ""
    torrentbytes_password = ""
    torrentbytes_ratio = ""
    torrentbytes_minseed = 1
    torrentbytes_minleech = 0
    torrentbytes_freeleech = 0
    torrentbytes_search_mode = eponly
    torrentbytes_search_fallback = 0
    torrentbytes_enable_daily = 1
    torrentbytes_enable_backlog = 1
    torrentbytes_cookies = ""
    [IPTORRENTS]
    iptorrents = 0
    iptorrents_custom_url = ""
    iptorrents_username = ""
    iptorrents_password = ""
    iptorrents_ratio = ""
    iptorrents_minseed = 1
    iptorrents_minleech = 0
    iptorrents_freeleech = 0
    iptorrents_search_mode = eponly
    iptorrents_search_fallback = 0
    iptorrents_enable_daily = 1
    iptorrents_enable_backlog = 1
    iptorrents_cookies = ""
    [NCORE_CC]
    ncore_cc = 0
    ncore_cc_username = ""
    ncore_cc_password = ""
    ncore_cc_ratio = ""
    ncore_cc_minseed = 1
    ncore_cc_minleech = 0
    ncore_cc_search_mode = eponly
    ncore_cc_search_fallback = 0
    ncore_cc_enable_daily = 1
    ncore_cc_enable_backlog = 1
    ncore_cc_cookies = ""
    [ILCORSARONERO]
    ilcorsaronero = 0
    ilcorsaronero_engrelease = 0
    ilcorsaronero_ratio = ""
    ilcorsaronero_minseed = 1
    ilcorsaronero_minleech = 0
    ilcorsaronero_search_mode = eponly
    ilcorsaronero_search_fallback = 0
    ilcorsaronero_enable_daily = 1
    ilcorsaronero_enable_backlog = 1
    ilcorsaronero_subtitle = 0
    ilcorsaronero_cookies = ""
    [MORETHANTV]
    morethantv = 0
    morethantv_username = ""
    morethantv_password = ""
    morethantv_ratio = ""
    morethantv_minseed = 1
    morethantv_minleech = 0
    morethantv_freeleech = 0
    morethantv_search_mode = eponly
    morethantv_search_fallback = 0
    morethantv_enable_daily = 1
    morethantv_enable_backlog = 1
    morethantv_cookies = ""
    [TVCHAOSUK]
    tvchaosuk = 0
    tvchaosuk_username = ""
    tvchaosuk_password = ""
    tvchaosuk_ratio = ""
    tvchaosuk_minseed = 1
    tvchaosuk_minleech = 0
    tvchaosuk_freeleech = 0
    tvchaosuk_search_mode = eponly
    tvchaosuk_search_fallback = 0
    tvchaosuk_enable_daily = 1
    tvchaosuk_enable_backlog = 1
    tvchaosuk_cookies = ""
    [LIMETORRENTS]
    limetorrents = 0
    limetorrents_ratio = ""
    limetorrents_minseed = 1
    limetorrents_minleech = 0
    limetorrents_search_mode = eponly
    limetorrents_search_fallback = 0
    limetorrents_enable_daily = 1
    limetorrents_enable_backlog = 1
    limetorrents_cookies = ""
    [SPEEDCD]
    speedcd = 0
    speedcd_username = ""
    speedcd_password = ""
    speedcd_ratio = ""
    speedcd_minseed = 1
    speedcd_minleech = 0
    speedcd_freeleech = 0
    speedcd_search_mode = eponly
    speedcd_search_fallback = 0
    speedcd_enable_daily = 1
    speedcd_enable_backlog = 1
    speedcd_cookies = ""
    [IMMORTALSEED]
    immortalseed = 0
    immortalseed_username = ""
    immortalseed_password = ""
    immortalseed_passkey = ""
    immortalseed_ratio = ""
    immortalseed_minseed = 1
    immortalseed_minleech = 0
    immortalseed_freeleech = 0
    immortalseed_search_mode = eponly
    immortalseed_search_fallback = 0
    immortalseed_enable_daily = 1
    immortalseed_enable_backlog = 1
    immortalseed_cookies = ""
    [DANISHBITS]
    danishbits = 0
    danishbits_username = ""
    danishbits_passkey = ""
    danishbits_ratio = ""
    danishbits_minseed = 1
    danishbits_minleech = 0
    danishbits_freeleech = 0
    danishbits_search_mode = eponly
    danishbits_search_fallback = 0
    danishbits_enable_daily = 1
    danishbits_enable_backlog = 1
    danishbits_cookies = ""
    [NYAA]
    nyaa = 0
    nyaa_confirmed = 1
    nyaa_ratio = ""
    nyaa_minseed = 1
    nyaa_minleech = 0
    nyaa_search_mode = eponly
    nyaa_search_fallback = 0
    nyaa_enable_daily = 1
    nyaa_enable_backlog = 1
    nyaa_cookies = ""
    [TORRENTDAY]
    torrentday = 0
    torrentday_custom_url = ""
    torrentday_username = ""
    torrentday_password = ""
    torrentday_ratio = ""
    torrentday_minseed = 1
    torrentday_minleech = 0
    torrentday_freeleech = 0
    torrentday_search_mode = eponly
    torrentday_search_fallback = 0
    torrentday_enable_daily = 1
    torrentday_enable_backlog = 1
    torrentday_cookies = ""
    [PRETOME]
    pretome = 0
    pretome_username = ""
    pretome_password = ""
    pretome_pin = ""
    pretome_ratio = ""
    pretome_minseed = 1
    pretome_minleech = 0
    pretome_search_mode = eponly
    pretome_search_fallback = 0
    pretome_enable_daily = 1
    pretome_enable_backlog = 1
    pretome_cookies = ""
    [YGGTORRENT]
    yggtorrent = 0
    yggtorrent_custom_url = ""
    yggtorrent_username = ""
    yggtorrent_password = ""
    yggtorrent_ratio = ""
    yggtorrent_minseed = 1
    yggtorrent_minleech = 0
    yggtorrent_search_mode = eponly
    yggtorrent_search_fallback = 0
    yggtorrent_enable_daily = 1
    yggtorrent_enable_backlog = 1
    yggtorrent_cookies = ""
    [SCENEACCESS]
    sceneaccess = 0
    sceneaccess_username = ""
    sceneaccess_password = ""
    sceneaccess_ratio = ""
    sceneaccess_minseed = 1
    sceneaccess_minleech = 0
    sceneaccess_search_mode = eponly
    sceneaccess_search_fallback = 0
    sceneaccess_enable_daily = 1
    sceneaccess_enable_backlog = 1
    sceneaccess_cookies = ""
    [NEWPCT]
    newpct = 1
    newpct_onlyspasearch = 0
    newpct_ratio = ""
    newpct_search_mode = eponly
    newpct_search_fallback = 0
    newpct_enable_daily = 1
    newpct_enable_backlog = 1
    newpct_cookies = ""
    [TOKYOTOSHOKAN]
    tokyotoshokan = 0
    tokyotoshokan_ratio = ""
    tokyotoshokan_minseed = 1
    tokyotoshokan_minleech = 0
    tokyotoshokan_search_mode = eponly
    tokyotoshokan_search_fallback = 0
    tokyotoshokan_enable_daily = 1
    tokyotoshokan_enable_backlog = 1
    tokyotoshokan_cookies = ""
    [HDTORRENTS]
    hdtorrents = 1
    hdtorrents_username = ""
    hdtorrents_password = ""
    hdtorrents_ratio = ""
    hdtorrents_minseed = 1
    hdtorrents_minleech = 0
    hdtorrents_freeleech = 0
    hdtorrents_search_mode = eponly
    hdtorrents_search_fallback = 0
    hdtorrents_enable_daily = 1
    hdtorrents_enable_backlog = 1
    hdtorrents_cookies = ""
    [THEPIRATEBAY]
    thepiratebay = 1
    thepiratebay_custom_url = ""
    thepiratebay_confirmed = 1
    thepiratebay_ratio = ""
    thepiratebay_minseed = 1
    thepiratebay_minleech = 0
    thepiratebay_search_mode = eponly
    thepiratebay_search_fallback = 0
    thepiratebay_enable_daily = 1
    thepiratebay_enable_backlog = 1
    thepiratebay_cookies = ""
    [TORRENT9]
    torrent9 = 0
    torrent9_ratio = ""
    torrent9_minseed = 1
    torrent9_minleech = 0
    torrent9_search_mode = eponly
    torrent9_search_fallback = 0
    torrent9_enable_daily = 1
    torrent9_enable_backlog = 1
    torrent9_cookies = ""
    [BITCANNON]
    bitcannon = 0
    bitcannon_custom_url = ""
    bitcannon_api_key = ""
    bitcannon_ratio = ""
    bitcannon_minseed = 1
    bitcannon_minleech = 0
    bitcannon_search_mode = eponly
    bitcannon_search_fallback = 0
    bitcannon_enable_daily = 1
    bitcannon_enable_backlog = 1
    bitcannon_cookies = ""
    [NEBULANCE]
    nebulance = 0
    nebulance_username = ""
    nebulance_password = ""
    nebulance_ratio = ""
    nebulance_minseed = 1
    nebulance_minleech = 0
    nebulance_freeleech = 0
    nebulance_search_mode = eponly
    nebulance_search_fallback = 0
    nebulance_enable_daily = 1
    nebulance_enable_backlog = 1
    nebulance_cookies = ""
    [ARCHETORRENT]
    archetorrent = 0
    archetorrent_username = ""
    archetorrent_password = ""
    archetorrent_ratio = ""
    archetorrent_minseed = 1
    archetorrent_minleech = 0
    archetorrent_freeleech = 0
    archetorrent_search_mode = eponly
    archetorrent_search_fallback = 0
    archetorrent_enable_daily = 1
    archetorrent_enable_backlog = 1
    archetorrent_cookies = ""
    [FILELIST]
    filelist = 0
    filelist_username = ""
    filelist_password = ""
    filelist_ratio = ""
    filelist_minseed = 1
    filelist_minleech = 0
    filelist_search_mode = eponly
    filelist_search_fallback = 0
    filelist_enable_daily = 1
    filelist_enable_backlog = 1
    filelist_cookies = ""
    [TORRENTLEECH]
    torrentleech = 0
    torrentleech_username = ""
    torrentleech_password = ""
    torrentleech_ratio = ""
    torrentleech_minseed = 1
    torrentleech_minleech = 0
    torrentleech_search_mode = eponly
    torrentleech_search_fallback = 0
    torrentleech_enable_daily = 1
    torrentleech_enable_backlog = 1
    torrentleech_cookies = ""
    [HDTORRENTS_IT]
    hdtorrents_it = 1
    hdtorrents_it_username = ""
    hdtorrents_it_password = ""
    hdtorrents_it_ratio = ""
    hdtorrents_it_minseed = 1
    hdtorrents_it_minleech = 0
    hdtorrents_it_freeleech = 0
    hdtorrents_it_search_mode = eponly
    hdtorrents_it_search_fallback = 0
    hdtorrents_it_enable_daily = 1
    hdtorrents_it_enable_backlog = 1
    hdtorrents_it_cookies = ""
    [NORBITS]
    norbits = 1
    norbits_username = ""
    norbits_passkey = ""
    norbits_ratio = ""
    norbits_minseed = 1
    norbits_minleech = 0
    norbits_search_mode = eponly
    norbits_search_fallback = 0
    norbits_enable_daily = 1
    norbits_enable_backlog = 1
    norbits_cookies = ""
    [HD4FREE]
    hd4free = 1
    hd4free_api_key = ""
    hd4free_username = ""
    hd4free_ratio = ""
    hd4free_minseed = 1
    hd4free_minleech = 0
    hd4free_freeleech = 0
    hd4free_search_mode = eponly
    hd4free_search_fallback = 0
    hd4free_enable_daily = 1
    hd4free_enable_backlog = 1
    hd4free_cookies = ""
    [NZBFINDER_WS]
    nzbfinder_ws = 0
    nzbfinder_ws_search_mode = eponly
    nzbfinder_ws_search_fallback = 0
    nzbfinder_ws_enable_daily = 1
    nzbfinder_ws_enable_backlog = 1
    nzbfinder_ws_cookies = ""
    [NZBS_ORG]
    nzbs_org = 0
    nzbs_org_search_mode = eponly
    nzbs_org_search_fallback = 0
    nzbs_org_enable_daily = 1
    nzbs_org_enable_backlog = 1
    nzbs_org_cookies = ""
    [OMGWTFNZBS]
    omgwtfnzbs = 0
    omgwtfnzbs_api_key = ""
    omgwtfnzbs_username = ""
    omgwtfnzbs_search_mode = eponly
    omgwtfnzbs_search_fallback = 0
    omgwtfnzbs_enable_daily = 1
    omgwtfnzbs_enable_backlog = 1
    omgwtfnzbs_cookies = ""
    [BINSEARCH]
    binsearch = 0
    binsearch_search_mode = eponly
    binsearch_search_fallback = 0
    binsearch_enable_daily = 0
    binsearch_enable_backlog = 0
    binsearch_cookies = ""
    [DOGNZB]
    dognzb = 0
    dognzb_search_mode = eponly
    dognzb_search_fallback = 0
    dognzb_enable_daily = 1
    dognzb_enable_backlog = 1
    dognzb_cookies = ""
    [NZB_CAT]
    nzb_cat = 0
    nzb_cat_search_mode = eponly
    nzb_cat_search_fallback = 0
    nzb_cat_enable_daily = 1
    nzb_cat_enable_backlog = 1
    nzb_cat_cookies = ""
    [NZBGEEK]
    nzbgeek = 0
    nzbgeek_search_mode = eponly
    nzbgeek_search_fallback = 0
    nzbgeek_enable_daily = 1
    nzbgeek_enable_backlog = 1
    nzbgeek_cookies = ""
    [USENET_CRAWLER]
    usenet_crawler = 0
    usenet_crawler_search_mode = eponly
    usenet_crawler_search_fallback = 0
    usenet_crawler_enable_daily = 1
    usenet_crawler_enable_backlog = 1
    usenet_crawler_cookies = ""
    [Newznab]
    newznab_data = "NZB.Cat|https://nzb.cat/||5030,5040,5010|0|eponly|0|1|1!!!NZBFinder.ws|https://nzbfinder.ws/||5030,5040,5010,5045|0|eponly|0|1|1!!!NZBGeek|https://api.nzbgeek.info/||5030,5040|0|eponly|0|1|1!!!NZBs.org|https://nzbs.org/||5030,5040|0|eponly|0|1|1!!!Usenet-Crawler|https://api.usenet-crawler.com/||5030,5040|0|eponly|0|1|1!!!DOGnzb|https://api.dognzb.cr/||5030,5040,5060,5070|0|eponly|0|1|1"
    [NZBs]
    nzbs = 0
    nzbs_uid = ""
    nzbs_hash = ""
    [Growl]
    growl_host = ""
    use_growl = 0
    growl_notify_ondownload = 0
    growl_notify_onsubtitledownload = 0
    growl_notify_onsnatch = 0
    growl_password = ""
    [Join]
    use_join = 0
    join_notify_onsnatch = 0
    join_notify_onsubtitledownload = 0
    join_apikey = ""
    join_notify_ondownload = 0
    join_id = ""
    [Slack]
    slack_notify_snatch = 0
    slack_notify_download = 0
    use_slack = 0
    slack_webhook = ""
    [Trakt]
    trakt_remove_serieslist = 0
    trakt_method_add = 0
    trakt_remove_watchlist = 1
    trakt_sync_watchlist = 1
    trakt_refresh_token = ""
    trakt_timeout = 30
    trakt_default_indexer = 1
    trakt_use_recommended = 0
    trakt_remove_show_from_sickrage = 0
    trakt_sync = 1
    use_trakt = 1
    trakt_blacklist_name = ""
    trakt_start_paused = 0
    trakt_access_token = ""
    trakt_sync_remove = 1
    trakt_username = \""""+trakt_user+"""\"
    [GUI]
    theme_name = dark
    coming_eps_missed_range = 7
    fanart_background_opacity = 0.4
    history_layout = detailed
    coming_eps_display_snatched = 0
    coming_eps_display_paused = 0
    gui_name = slick
    custom_css_path = ""
    fuzzy_dating = 0
    poster_sortdir = 1
    poster_sortby = name
    trim_zero = 0
    sickrage_background_path = ""
    date_preset = %x
    home_layout = poster
    coming_eps_layout = banner
    coming_eps_sort = date
    time_preset = %I:%M:%S %p
    timezone_display = local
    sickrage_background = 0
    custom_css = 0
    display_show_specials = 1
    language = ""
    fanart_background = 1
    history_limit = 100
    [NMA]
    nma_notify_onsubtitledownload = 0
    use_nma = 0
    nma_notify_onsnatch = 0
    nma_priority = 0
    nma_api = ""
    nma_notify_ondownload = 0
    [TorrentRss]
    torrentrss_data = ""
    [Prowl]
    prowl_notify_ondownload = 0
    prowl_api = ""
    prowl_message_title = SickRage
    prowl_priority = 0
    prowl_notify_onsubtitledownload = 0
    prowl_notify_onsnatch = 0
    use_prowl = 0
    [Shares]
    [Newzbin]
    newzbin = 0
    newzbin_password = ""
    newzbin_username = ""
    [Synology]
    username = ""
    path = ""
    host = ""
    password = ""
    use_synoindex = 0
    [NMJv2]
    nmjv2_dbloc = ""
    nmjv2_database = ""
    nmjv2_host = ""
    use_nmjv2 = 0
    [SABnzbd]
    sab_forced = 0
    sab_category = tv
    sab_apikey = ""
    sab_category_anime = anime
    sab_category_backlog = tv
    sab_host = ""
    sab_password = ""
    sab_username = ""
    sab_category_anime_backlog = anime
    [Plex]
    plex_client_password = ""
    plex_server_username = ""
    plex_server_https = 0
    plex_server_password = ""
    plex_server_host = ""
    plex_notify_onsubtitledownload = 0
    plex_notify_onsnatch = 0
    plex_server_token = ""
    plex_client_host = ""
    plex_client_username = ""
    use_plex_client = 0
    plex_update_library = 0
    plex_notify_ondownload = 0
    use_plex_server = 0
    [TORRENT]
    torrent_verify_cert = 0
    torrent_paused = 0
    torrent_host = http://192.168.200.44:9091/habita/torrent
    torrent_label_anime = ""
    torrent_path = ""
    torrent_auth_type = none
    torrent_rpcurl = transmission
    torrent_username = """+transmission_user+"""
    torrent_label = ""
    torrent_password = """+transmission_pass+"""
    torrent_high_bandwidth = 0
    torrent_seed_time = 0
    [Pushalot]
    pushalot_notify_onsubtitledownload = 0
    pushalot_authorizationtoken = ""
    pushalot_notify_onsnatch = 0
    pushalot_notify_ondownload = 0
    use_pushalot = 0
    [Pushover]
    pushover_notify_ondownload = 0
    pushover_sound = pushover
    use_pushover = 0
    pushover_notify_onsubtitledownload = 0
    pushover_priority = 0
    pushover_device = ""
    pushover_apikey = ""
    pushover_userkey = ""
    pushover_notify_onsnatch = 0
    [Email]
    email_notify_onsnatch = 0
    email_list = ""
    email_password = ""
    email_subject = ""
    email_tls = 0
    use_email = 0
    email_notify_ondownload = 0
    email_port = 25
    email_notify_onsubtitledownload = 0
    email_user = ""
    email_from = ""
    email_host = ""
    [KODI]
    kodi_update_onlyfirst = 0
    kodi_notify_onsnatch = 0
    kodi_notify_ondownload = 1
    kodi_host = 127.0.0.1:8080
    kodi_username = osmc
    kodi_always_on = 1
    kodi_update_library = 1
    use_kodi = 1
    kodi_password = formen5hongkong
    kodi_update_full = 0
    kodi_notify_onsubtitledownload = 0
    [Telegram]
    telegram_notify_ondownload = 0
    telegram_apikey = ""
    telegram_id = ""
    use_telegram = 0
    telegram_notify_onsnatch = 0
    telegram_notify_onsubtitledownload = 0
    [FreeMobile]
    freemobile_notify_onsnatch = 0
    freemobile_notify_onsubtitledownload = 0
    freemobile_notify_ondownload = 0
    freemobile_apikey = ""
    freemobile_id = ""
    use_freemobile = 0
    [Discord]
    discord_notify_download = 0
    discord_notify_snatch = 0
    discord_webhook = ""
    use_discord = 0
    [SynologyNotifier]
    synologynotifier_notify_onsnatch = 0
    synologynotifier_notify_ondownload = 0
    use_synologynotifier = 0
    synologynotifier_notify_onsubtitledownload = 0
    [ANIDB]
    anidb_use_mylist = 0
    use_anidb = 0
    anidb_password = ""
    anidb_username = ""
    [Blackhole]
    nzb_dir = ""
    torrent_dir = ""
    [General]
    naming_anime_multi_ep = 1
    use_nzbs = 0
    log_size = 10.0
    git_remote = origin
    use_icacls = 1
    season_folders_default = 1
    web_ipv6 = 0
    anime_default = 0
    metadata_wdtv = 0|0|0|0|0|0|0|0|0|0
    default_page = home
    update_frequency = 1
    naming_anime_pattern = Season %0S/%SN - S%0SE%0E - %EN
    encryption_version = 0
    https_key = server.key
    processor_follow_symlinks = 0
    allow_high_priority = 1
    developer = 0
    anon_redirect = http://dereferer.org/?
    indexer_timeout = 20
    naming_anime = 3
    metadata_mede8er = 0|0|0|0|0|0|0|0|0|0
    naming_custom_sports = 0
    debug = 0
    metadata_tivo = 0|0|0|0|0|0|0|0|0|0
    dailysearch_frequency = 40
    download_url = ""
    naming_custom_anime = 0
    ignore_words = "german,french,core2hd,dutch,swedish,reenc,MrLss"
    root_dirs = 0|"""+rename_dir+"""
    delete_non_associated_files = 1
    api_key = bf712e0ae92389505e442ebff292f4a6
    randomize_providers = 0
    web_host = 0.0.0.0
    config_version = 8
    check_propers_interval = daily
    nzb_method = blackhole
    process_automatically = 1
    calendar_unprotected = 0
    sync_files = "!sync,lftp-pget-status,bts,!qb,!qB"
    git_path = ""
    web_cookie_secret = IKpKJ6f4RAWDY2OxYzuBm3wBR6pKwEixvzJUKUvPsBM=
    news_last_read = 2017-08-05
    ssl_verify = 1
    handle_reverse_proxy = 0
    launch_browser = 1
    unpack = 0
    cur_commit_hash = 61a763d303f7337709e03a76b01d9592e2dce14d
    move_associated_files = 0
    status_default = 3
    naming_multi_ep = 1
    encryption_secret = /NarkX7nTYiqyZrAGKL3vnSJ4eW9pUnsoqr2x0eI++E=
    torrent_method = transmission
    localhost_ip = ""
    use_listview = 0
    version_notify = 1
    enable_https = 0
    naming_custom_abd = 0
    allowed_extensions = "nfo,srr,sfv,srt"
    web_root = ""
    add_shows_wo_dir = 0
    cur_commit_branch = ""
    indexer_default = 0
    use_torrents = 1
    display_all_seasons = 1
    no_delete = 0
    usenet_retention = 500
    naming_abd_pattern = %SN - %A.D - %EN
    download_propers = 1
    use_free_space_check = 1
    socket_timeout = 30
    proxy_setting = ""
    del_rar_contents = 0
    backlog_frequency = 720
    no_restart = 0
    notify_on_login = 0
    trash_remove_show = 0
    process_method = symlink
    metadata_ps3 = 0|0|0|0|0|0|0|0|0|0
    ignore_broken_symlinks = 0
    showupdate_hour = 4
    quality_default = 336
    alt_unrar_tool = bsdtar
    file_timestamp_timezone = network
    require_words = ""
    git_username = ""
    auto_update = 1
    git_remote_url = https://github.com/SickRage/SickRage.git
    tv_download_dir = """+download_dir+"""
    trackers_list = "udp://coppersurfer.tk:6969/announce,udp://open.demonii.com:1337,udp://exodus.desync.com:6969,udp://9.rarbg.me:2710/announce,udp://glotorrents.pw:6969/announce,udp://tracker.openbittorrent.com:80/announce,udp://9.rarbg.to:2710/announce"
    git_auth_type = 0
    extra_scripts = ""
    git_token_password = ""
    web_use_gzip = 1
    indexerDefaultLang = en
    log_dir = Logs
    branch = master
    autopostprocessor_frequency = 10
    unrar_tool = unrar
    git_password = ""
    ep_default_deleted_status = 6
    rename_episodes = 1
    metadata_mediabrowser = 0|0|0|0|0|0|0|0|0|0
    naming_sports_pattern = %SN - %A-D - %EN
    create_missing_show_dirs = 0
    trash_rotate_logs = 0
    naming_strip_year = 0
    airdate_episodes = 0
    proxy_indexers = 1
    web_log = 0
    log_nr = 5
    git_reset = 1
    web_password = """+password+"""
    provider_order = horriblesubs rarbg torrentz newpct hd4free skytorrents hounddawgs hdbits abnormal hdtorrents thepiratebay hdtorrents_it norbits alpharatio scenetime gftracker hdspace btn elitetorrent cpasbien tntvillage xthor shazbat_tv torrentproject torrentbytes iptorrents ncore_cc ilcorsaronero morethantv tvchaosuk limetorrents speedcd immortalseed danishbits nyaa torrentday pretome yggtorrent sceneaccess tokyotoshokan torrent9 bitcannon nebulance archetorrent filelist torrentleech
    https_cert = server.crt
    scene_default = 0
    backlog_days = 7
    notify_on_update = 1
    skip_removed_files = 0
    status_default_after = 3
    naming_pattern = Season %0S/%SN - S%0SE%0E - %EN
    sort_article = 0
    web_port = 8081
    web_username = """+user+"""
    dbdebug = 0
    unpack_dir = ""
    ignored_subs_list = "dk,fin,heb,kor,nor,nordic,pl,swe"
    calendar_icons = 0
    postpone_if_sync_files = 1
    metadata_kodi = 0|0|0|0|0|0|0|0|0|0
    cpu_preset = NORMAL
    cache_dir = cache
    nfo_rename = 1
    metadata_kodi_12plus = 0|0|0|0|0|0|0|0|0|0
    keep_processed_dir = 0
    [NZBget]
    nzbget_host = ""
    nzbget_category_anime = anime
    nzbget_use_https = 0
    nzbget_password = tegbzn6789
    nzbget_category = tv
    nzbget_priority = 100
    nzbget_category_anime_backlog = anime
    nzbget_username = nzbget
    nzbget_category_backlog = tv
    [Emby]
    use_emby = 0
    emby_apikey = ""
    emby_host = ""
    [pyTivo]
    pytivo_share_name = ""
    pytivo_notify_ondownload = 0
    pytivo_tivo_name = ""
    pytivo_notify_onsnatch = 0
    pytivo_host = ""
    pytivo_notify_onsubtitledownload = 0
    pyTivo_update_library = 0
    use_pytivo = 0
    [Pushbullet]
    pushbullet_channel = ""
    pushbullet_device = ""
    use_pushbullet = 0
    pushbullet_notify_ondownload = 0
    pushbullet_notify_onsubtitledownload = 0
    pushbullet_notify_onsnatch = 0
    pushbullet_api = ""
    [Twilio]
    twilio_account_sid = ""
    twilio_notify_ondownload = 0
    use_twilio = 0
    twilio_notify_onsubtitledownload = 0
    twilio_to_number = ""
    twilio_notify_onsnatch = 0
    twilio_phone_sid = ""
    twilio_auth_token = ""
    [Libnotify]
    libnotify_notify_onsubtitledownload = 0
    libnotify_notify_onsnatch = 0
    libnotify_notify_ondownload = 0
    use_libnotify = 0
    [Boxcar2]
    use_boxcar2 = 0
    boxcar2_notify_onsnatch = 0
    boxcar2_notify_ondownload = 0
    boxcar2_accesstoken = ""
    boxcar2_notify_onsubtitledownload = 0
    [FailedDownloads]
    use_failed_downloads = 0
    delete_failed = 0
    [NMJ]
    nmj_host = ""
    nmj_mount = ""
    use_nmj = 0
    nmj_database = ""
    [Twitter]
    twitter_username = ""
    use_twitter = 0
    twitter_password = ""
    twitter_notify_ondownload = 0
    twitter_notify_onsubtitledownload = 0
    twitter_notify_onsnatch = 0
    twitter_prefix = SickRage
    twitter_dmto = ""
    twitter_usedm = 0
    [Subtitles]
    opensubtitles_password = ""
    itasa_password = ""
    subtitles_keep_only_wanted = 0
    addic7ed_username = ""
    legendastv_username = ""
    subtitles_include_specials = 1
    legendastv_password = ""
    subscenter_username = ""
    subtitles_default = 0
    subtitles_multi = 1
    subtitles_extra_scripts = ""
    opensubtitles_username = ""
    embedded_subtitles_all = 0
    subtitles_history = 0
    subtitles_hearing_impaired = 0
    itasa_username = ""
    subtitles_languages = "eng,spa"
    subtitles_finder_frequency = 1
    subtitles_perfect_match = 1
    SUBTITLES_SERVICES_LIST = "addic7ed,legendastv,opensubtitles,podnapisi,shooter,thesubdb,tvsubtitles,itasa,wizdom,subscenter"
    addic7ed_password = ""
    use_subtitles = 1
    subtitles_dir = ""
    subscenter_password = ""
    SUBTITLES_SERVICES_ENABLED = 0|0|1|0|0|0|0|0|0|0
    [ANIME]
    anime_split_home_in_tabs = 0
    anime_split_home = 0
    [BJ_SHARE]
    bj_share = 0
    bj_share_username = ""
    bj_share_password = ""
    bj_share_ratio = ""
    bj_share_minseed = 1
    bj_share_minleech = 0
    bj_share_search_mode = eponly
    bj_share_search_fallback = 0
    bj_share_enable_daily = 1
    bj_share_enable_backlog = 1
    bj_share_cookies = ""
    [GIMMEPEERS]
    gimmepeers = 0
    gimmepeers_username = ""
    gimmepeers_password = ""
    gimmepeers_ratio = ""
    gimmepeers_minseed = 1
    gimmepeers_minleech = 0
    gimmepeers_search_mode = eponly
    gimmepeers_search_fallback = 0
    gimmepeers_enable_daily = 1
    gimmepeers_enable_backlog = 1
    gimmepeers_cookies = ""
    """

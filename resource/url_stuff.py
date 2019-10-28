url_endings = [
    "com","org","net","int",
    "edu","gov","mil",
    'ac','ad','ae','af','ag','ai',
    'al','am','an','ao','aq','ar',
    'as','at','au','aw','ax','az',
    'ba','bb','bd','be','bf','bg',
    'bh','bi','bj','bm','bn','bo',
    'br','bs','bt','bw','by','bz',
    'ca','cc','cd','cf','cg','ch',
    'ci','ck','cl','cm','cn','co',
    'cr','cu','cv','cw','cx','cy',
    'cz','de','dj','dk','dm','do',
    'dz','ec','ee','eg','es','et',
    'eu','fi','fj','fk','fm','fo',
    'fr','ga','gd','ge','gf','gg',
    'gh','gi','gl','gm','gn','gp',
    'gq','gr','gs','gt','gu','gw',
    'gy','hk','hm','hn','hr','ht',
    'hu','id','ie','il','im','in',
    'io','iq','ir','is','it','je',
    'jm','jo','jp','ke','kg','kh',
    'ki','km','kn','kp','kr','kw',
    'ky','kz','la','lb','lc','li',
    'lk','lr','ls','lt','lu','lv',
    'ly','ma','mc','md','me','mg',
    'mh','mk','ml','mm','mn','mo',
    'mp','mq','mr','ms','mt','mu',
    'mv','mw','mx','my','mz','na',
    'nc','ne','nf','ng','ni','nl',
    'no','np','nr','nu','nz','om',
    'pa','pe','pf','pg','ph','pk',
    'pl','pm','pn','pr','ps','pt',
    'pw','py','qa','re','ro','rs',
    'ru','rw','sa','sb','sc','sd',
    'se','sg','sh','si','sk','sl',
    'sm','sn','so','sr','ss','st',
    'su','sv','sx','sy','sz','tc',
    'td','tf','tg','th','tj','tk',
    'tl','tm','tn','to','tr','tt',
    'tv','tw','tz','ua','ug','uk',
    'us','uy','va','vc','ve','vg',
    'vi','vn','vu','wf','ws','ye',
    'yt','za','zm','zw',
    'academy','accountants','active',
    'actor','ads','adult','aero',
    'africa','agency','airforce',
    'analytics','apartments','app',
    'archi','army','art','associates',
    'attorney','auction','audible',
    'audio','author','auto','autos',
    'aws','baby','band','bank',
    'bar','barefoot','bargains',
    'baseball','basketball','beauty',
    'beer','best','bestbuy','bet',
    'bible','bid','bike','bingo',
    'bio','biz','black','blackfriday',
    'blog','blue','boo','book',
    'boots','bot','boutique','box',
    'broadway','broker','build',
    'builders','business','buy',
    'buzz','cab','cafe','call','cam',
    'camera','camp','cancerresearch',
    'capital','car','cards','care',
    'career','careers','cars','case',
    'cash','casino','catering',
    'catholic','center',' cern','ceo',
    'cfd','channel','chat','cheap',
    'christmas','church','cipriani',
    'circle','city','claims',
    'cleaning','click','clinic',
    'clothing','cloud','club','coach',
    'codes','data','design','dev',
    'directory','download','eco',
    'education','email','events',
    'exchange','exposed']

def url_return(message):
    space_split = message.content.split(" ")
    for i in space_split:
        for ii in url_endings:
            if ".%s/" % ii in i:
                return i

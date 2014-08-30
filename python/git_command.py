data = {
  'old_words' : {
    'template' : ['{old_disease}', '{old_units}', '{old_technology}', '{old_science}'],

    #Source: http://en.wikipedia.org/wiki/List_of_deprecated_terms_for_diseases
    'old_disease' : ['apoplexy', 'bilious', 'consumption', 'dropsy', 'front-street', 'gleet', 'grippe', 'lockjaw', 'norwalk', 'phthisis', 'quinsy', 'squinsy', 'undulant'],

    #Source: http://en.wikipedia.org/wiki/Category:Obsolete_units_of_measurement
    'old_units' : ['abucco', 'adowlie', 'angula', 'atom', 'bahar', 'buddam', 'carcel', 'carucate', 'cawnie', 'chungah', 'coomb', 'corgee', 'cubit', 'cullingey', 'cullishigay', 'delisle', 'dessiatin', 'dharni', 'dirham', 'ell', 'fanega', 'firlot', 'garce', 'girah', 'grzywna', 'guz', 'hekat', 'hobbit', 'homer', 'juchart', 'katha', 'koku', 'kula', 'ligne', 'mache', 'marabba', 'metretes', 'morgen', 'munjandie', 'oka', 'oxgang', 'peck', 'perch', 'poncelet', 'pood', 'spat', 'toise', 'unglie', 'wey', 'yojana', 'zentner', 'zolotnik', 'ordlach'],

    #Source: http://en.wikipedia.org/wiki/Category:Obsolete_technologies
    'old_technology' : ['ballista', 'calculagraph', 'carriage', 'catapult', 'kinescope', 'mimeograph', 'multi-image', 'pulse-dial', 'rotary', 'stauroscope', 'sundial'],

    #Source: http://en.wikipedia.org/wiki/Category:Obsolete_scientific_theories
    'old_science' : ['adamic', 'aether', 'antiperistasis', 'barlow', 'caloric', 'corpuscular', 'cyclol', 'dark-star', 'dualism', 'enochian', 'etheric', 'firmament', 'galactocentrism', 'geohumoral', 'vacui', 'imponderable', 'japhetic', 'quasar', 'lescarbault', 'limbic', 'luminiferous', 'milne', 'phrenol', 'polflucht', 'recapitulation', 'reticular', 'sublunary', 'impetus', 'thomson-berthelot', 'troidal', 'trepidation', 'tychonic', 'vulcan'],

    #Possible other source: http://en.wikipedia.org/wiki/Category:Obsolete_taxonomic_groups, http://en.wikipedia.org/wiki/Category:Modern_obsolete_currencies, http://en.wikipedia.org/wiki/Category:Former_entities
  },

  'git_command' : {
    'template' : ['{real_command}'],

    'real_command' : ['config', 'help', 'init', 'clone', 'add', 'status', 'diff', 'commit', 'reset', 'rm', 'mv', 'branch', 'checkout', 'merge', 'mergetool', 'log', 'stash', 'tag', 'fetch', 'pull', 'push', 'remote', 'submodule', 'show', 'log', 'diff', 'shortlog', 'describe', 'apply', 'cherry-pick', 'diff', 'rebase', 'revert', 'bisect', 'blame', 'grep', 'am', 'apply', 'format-patch', 'send-email', 'request-pull', 'svn', 'fast-import', 'clean', 'gc', 'fsck', 'reflog', 'filter-branch', 'instaweb', 'archive', 'daemon', 'update-server-info', 'cat-file', 'commit-tree', 'count-objects', 'diff-index', 'for-each-ref', 'hash-object', 'ls-files', 'merge-base', 'read-tree', 'rev-list', 'rev-parse', 'show-ref', 'symbolic-ref', 'update-index', 'update-ref', 'verify-pack', 'write-tree']
  },

  'git_short_desc' : {
    'template' : ['{template} or {template}', '{verb} {thing}', '{verb} {thing} from {thing}', '{verb} {thing} {transition} {thing}'],

    'thing' : ['{article} {adjective} {noun}', '{adjective} {nouns}', '{proper_noun}'],

    'article' : ['a', 'the'],

    'transition' : ['into', 'towards', 'using'],

    'proper_noun' : ['Git', 'Linux', 'Unix', 'GNU'],

    'noun' : ['{noun_tech}'],
    'noun_tech' : ['tree', 'file', 'repository', 'option', 'terminal', 'shell', 'directory'],

    'nouns' : ['{nouns_tech}'],
    'nouns_tech' : ['trees', 'files', 'repositories', 'options', 'terminals', 'shells', 'directories', 'information about {thing}'],

    'adjective' : ['{adj_standard}', '{adj_tech}'],
    'adj_standard' : ['global', 'local', 'standard', 'helpful', 'empty', 'existing'],
    'adj_tech' : ['working', 'bitwise', 'untracked', 'tracked', 'binary', 'encoded'],

    'verb' : ['{verb} and {verb}', '{verb_standard}', '{verb_tech}'],
    'verb_standard' : ['show', 'get', 'set', 'modify', 'display'],
    'verb_tech' : ['invert', 'hash', 'upload', 'download', 'sync', 'create', 'reinitialize', 'clone']
  },

  'git_synopsis' : {
    'template' : ["'git {username}' {terms}"],

    'terms' : ['{terms} {terms}', '{terms} [{term}]', '[{term}]'],

    'term' : ['{term} <{option}>', '-{gen/vowel}', '-{gen/consonant}', '--{old_words/template}'],

    'option' : ['{old_words/template}'],
  },

  'git_desc' : {
    'template' : []
  }
}
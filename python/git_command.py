data = {
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
    'template' : ["'git {username}'"],


  },

  'git_desc' : {
    'template' : []
  }
}
class GitController < ApplicationController
  def index
    @tagline = 'in-dev-forever'
    @command_name = %x(python python/generate_info.py git_command)
    @command_desc = %x(python python/generate_info.py git_short_desc #{@command_name})
    @command_synopsis = %x(python python/generate_info.py git_synopsis #{@command_name})
    @version_num = '2.1.0'
  end
end

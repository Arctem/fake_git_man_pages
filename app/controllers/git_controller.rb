class GitController < ApplicationController
  def index
    #handle params
    @command_name = params[:command]

    @tagline = 'in-dev-forever'
    @command_name = %x(python python/generate_info.py git_command) unless @command_name
    @command_desc = %x(python python/generate_info.py git_short_desc #{@command_name})
    @command_synopsis = %x(python python/generate_info.py git_synopsis #{@command_name})
    @command_synopsis = @command_synopsis.scan(/.{1,60}]/).join("\n")
    @version_num = '2.1.0'
  end
end

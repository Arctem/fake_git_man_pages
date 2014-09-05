Rails.application.routes.draw do
  root 'git#index'
  get '/docs/:command', to: 'git#index'
end

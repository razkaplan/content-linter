source "https://rubygems.org"

gem "jekyll", "~> 3.9.0" # Downgrade Jekyll to a compatible version
gem "minima", "~> 2.1.1" # Downgrade Minima to a compatible version

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.9.2" # Downgrade jekyll-feed to a compatible version
  gem "jekyll-sitemap"
  gem "jekyll-paginate"
end

gem "logger"
gem "csv"

platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
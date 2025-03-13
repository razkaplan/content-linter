# filepath: /Users/razkaplan/Documents/GitHub/GTM/_plugins/posthog.rb
require 'posthog-ruby'

PostHog.init({
  api_key: 'phc_GcBoLEsaW7xx4EDrB2ZIpecfwcmC9rHOwJrt9vbTdvT',
  api_host: 'https://eu.i.posthog.com'
})

Jekyll::Hooks.register :site, :post_write do |site|
  site.pages.each do |page|
    PostHog.capture({
      distinct_id: 'site_visitor',
      event: 'Page Viewed',
      properties: {
        title: page.data['title'],
        url: page.url
      }
    })
  end
end
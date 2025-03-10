---
layout: default
title: Home
---

<div class="max-w-4xl mx-auto p-6 space-y-8">
  <!-- Hero Section -->
  <section class="text-center space-y-4">
    <h1 class="text-4xl font-bold">Headless Marketing - Empowering Founders to Scale with Confidence</h1>
    <p class="text-lg text-gray-600">Expert guidance and hanns on execution for technical founders to establish robust Go-to-Market strategies—efficiently and effectively.</p>
  </section>

<!-- Pain Points -->
<!--
<section class="space-y-4">
    <h2 class="text-2xl font-semibold">Common Founder Challenges</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        {% for pain in site.data.pain_points %}
        <div class="card flex items-center space-x-3 p-4 border rounded-lg shadow-sm">
            <span class="text-2xl">{{ pain.icon }}</span>
            <p>{{ pain.text }}</p>
        </div>
        {% endfor %}
    </div>
</section>
-->

  <!-- Blog Section -->
  <section class="space-y-4">
    <h2 class="text-2xl font-semibold">Latest Insights - My Blog</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      {% for post in site.posts limit:3 %}
      <div class="card p-4 border rounded-lg shadow-sm">
        <h3 class="text-lg font-semibold"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
        <p>{{ post.summary }}</p>
        <p><a href="{{ site.baseurl }}{{ post.url }}">Read</a></p>
        ---
      </div>
      {% endfor %}
    </div>
  </section>

  <!-- Services Section -->
  <section class="space-y-4">
    <h2 class="text-2xl font-semibold">How I Can Help</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      {% for service in site.data.services %}
      <div class="card p-4 border rounded-lg shadow-sm">
        <p class="text-lg font-semibold"> {{ service.title }}: <a href="{{ service.link }} " target="_blank" class="text-blue-500 underline">{{ service.description }}</a>  </p>
        </div>
      {% endfor %}
    </div>
  </section>
---

  <!-- Tools Section -->

<!--
  <section class="space-y-4">
    <h2 class="text-2xl font-semibold">Marketing Tools</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      {% for tool in site.data.tools %}
      <div class="card p-4 border rounded-lg shadow-sm">
        <p class="text-lg font-semibold"> {{ tool.title }}: <a href="{{ tool.link }}" class="text-blue-500 underline">{{ tool.description }}</a>  </p>
      </div>
      {% endfor %}
    </div>
  </section> 
-->

  <!-- AI Fun Projects -->
  <section class="space-y-4">
    <h2 class="text-2xl font-semibold">AI Projects for Fun</h2>
    <p>Some cool AI experiments and side projects I’ve built:</p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      {% for project in site.data.projects limit:3 %}
      <div class="card p-4 border rounded-lg shadow-sm">
        <P class="text-lg font-semibold"><a href="{{ project.url }} " target="_blank">{{ project.title }}</a> - {{ project.description }}</p>
        ---
      </div>
      {% endfor %}
    </div>
  </section>

  <!-- About Me Section -->
  <section class="space-y-4">
    <section class="space-y-4">
        <h2 class="text-2xl font-semibold">About Me</h2>
        <p>{{ site.description }}</p>
    </section>
  </section>


    <p>&copy; {{ 'now' | date: '%Y' }} All rights reserved.</p>
</div>

<!-- PostHog Analytics -->
<script>
    !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture register register_once register_for_session unregister unregister_for_session getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty createPersonProfile opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing clear_opt_in_out_capturing debug getPageViewId captureTraceFeedback captureTraceMetric".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
    posthog.init('phc_GcBoLEsaW7xx4EDrB2ZIpecfwcmC9rHOwJrt9vbTdvT', {
        api_host: 'https://eu.i.posthog.com',
        person_profiles: 'identified_only', // or 'always' to create profiles for anonymous users as well
    })
</script>

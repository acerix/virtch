import { FunctionalComponent, h } from 'preact'
import { Router } from 'preact-router'
import Helmet from 'react-helmet'

import Home from '../routes/home'
import Play from '../routes/play'
import NotFound from '../routes/not-found'
import Header from './header'
import Footer from './footer'

const App: FunctionalComponent = () => {
  return (
    <div>
      <Helmet
        htmlAttributes={{lang: "en-CA", amp: undefined}}
        title="No Title" titleTemplate="%s — Virtch.io"
        titleAttributes={{itemprop: "name", lang: "en-CA"}}
        meta={[
          {name: "description", content: "Virtch.io is an online community dedicated to wasting your time. We deliver cutting-edge time-suckers and related paraphernalia."}
        ]}
        link={[
          {rel: "canonical", href: "https://virtch.io/"},
        ]}
        script={[
          {type: "application/ld+json", innerHTML: `{
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "Virtch.io",
            "legalName" : "Virtch Incorporated",
            "url": "https://virtch.io",
            "logo": "https://virtch.io/assets/Virtch-logo.png",
            "foundingDate": "2020-10-30",
            "founders": [
              {
              "@type": "Person",
              "name": "Dylan Ferris"
              }
            ],
            "email": "support@virtch.io"
          }`}
        ]}
      />
      <Header />
      <main>
        <Router>
          <Home path="/" />
          <Play path="/play/" />
          <NotFound path="/404/" />
          <NotFound default />
        </Router>
      </main>
      <Footer />
    </div>
  )
}

export default App

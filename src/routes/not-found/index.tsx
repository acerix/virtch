import { FunctionalComponent, h } from 'preact'
import Helmet from 'react-helmet'
import { Link } from 'preact-router/match'

const NotFound: FunctionalComponent = () => {
  return (
    <section class="container py-5">
      <Helmet title="Page Not Found" />
      <h1>Page Not Found — Error 404</h1>
      <p>Why u do this?</p>
      <Link href="/">
         Go Home
      </Link>
    </section>
  )
}

export default NotFound

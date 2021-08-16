import { FunctionalComponent, h } from 'preact'
import Helmet from 'react-helmet'
import { Link } from 'preact-router/match'

const Home: FunctionalComponent = () => {
  return (
    <section class="container">
      <Helmet title="Home" />
      <div class="px-4 pt-5 my-5 text-center border-bottom">
        <h1 class="h4 fw-bold">Virtch.io</h1>
        <div class="col-lg-6 mx-auto">
          <p class="lead mb-4">Sucking up virtually all time since 2021.</p>
          <div class="d-grid gap-2 d-sm-flex justify-content-sm-center mb-5">
            <Link class="btn btn-outline-primary btn-lg px-4 me-sm-3" href="/play/">
              Play
            </Link>
          </div>
        </div>
      </div>
    </section>
  )
}

export default Home

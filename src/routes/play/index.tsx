import { FunctionalComponent, h } from 'preact'
import Helmet from 'react-helmet'

const Play: FunctionalComponent = () => {
  return (
    <section class="container">
      <Helmet title="Play" />
      <div class="px-4 pt-5 my-5 text-center border-bottom">
        <h1 class="h4 fw-bold">Play</h1>
        <p>Now wut?</p>
      </div>
    </section>
  )
}

export default Play

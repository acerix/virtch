import { h } from 'preact'
import Play from '../src/routes/play'
import { shallow } from 'enzyme'

describe('Test play page', () => {
  test('Home header is as expected', () => {
    const context = shallow(<Play />)
    expect(context).toBeTruthy()
  })
})

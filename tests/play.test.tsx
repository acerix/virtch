import { h } from 'preact'
import Play from '../src/routes/play'
import { shallow } from 'enzyme'

describe('Test home page contents', () => {
  test('Home header is as expected', () => {
    const context = shallow(<Play />)
    expect(context.find('h1').text()).toBe('Play')
  })
})

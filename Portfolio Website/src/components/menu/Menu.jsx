import "./menu.scss"

export default function Menu({ menuOpen, setMenuOpen }) {
  return (
  <div className = {"menu " + (menuOpen && 'active')}> {/* you can actually save the LIs as a component and use the onClick function like we did before*/}
      <ul>
          <li onClick={()=>setMenuOpen(false)}> {/*not best practices copied and pasted multiple times need to fix in the futrue*/}
              <a href="#intro">Home</a>
          </li>
      </ul>
      <ul>
          <li onClick={()=>setMenuOpen(false)}>
              <a href="#portfolio">Portfolio</a>
          </li>
      </ul>
      <ul>
          <li onClick={()=>setMenuOpen(false)}>
              <a href="#works">Works</a>
          </li>
      </ul>
      <ul>
          <li onClick={()=>setMenuOpen(false)}>
              <a href="#testimonials">Testimonials</a>
          </li>
      </ul>
      <ul>
          <li onClick={()=>setMenuOpen(false)}>
              <a href="#contact">Contact</a>
          </li>
      </ul>

  </div>
  )
}

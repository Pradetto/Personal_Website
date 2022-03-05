import "./topbar.scss";
import {Person,Mail} from "@material-ui/icons"

export default function Topbar({ menuOpen, setMenuOpen }) {
  return (
  <div className={"topbar " + (menuOpen && "active")}> {/*remove active to toggle top bar color*/}
    <div className="wrapper">
      <div className="left">
        <a href="#intro" className="logo">Pradetto.</a> 
        <div className="itemContainer">
          <Person className="icon"/>
          <span>817-676-8533</span>
        </div>
        <div className="itemContainer">
          <Mail className="icon"/>
          <span>pradetto5@gmail.com</span>
        </div>
      </div>
      center here boiii
      <div className="right">
        <div className="hamburger" onClick={()=>setMenuOpen(!menuOpen)}>
          <span className="line1"> </span>
          <span className="line2"> </span>
          <span className="line3"> </span>
        </div>
      </div>
    </div>
  </div>
  )
}


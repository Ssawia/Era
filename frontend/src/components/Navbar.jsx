import { Link } from "react-router-dom";
import "../css/Navbar.css"

function NavBar(){

    return(
        <nav className="navbar">

            <div className="navbar-brand"> 
                <Link to="/">Character App</Link>
            </div>
            
            <div className="navbar-brand"> 
                <Link to="/" className="nav-link">Home</Link>
                <Link to="/favorites" className="nav-link">Favorites</Link>
            </div>

        </nav>

    )
}

export default NavBar
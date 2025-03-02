import CharacterCard from "../components/CharacterCard"
import { useState, useEffect } from "react"
import "../css/Home.css"
import { getCharacters, addCharacters } from "../services/api";

function Home(){
    const [searchQuery, setSearchQuery] = useState("");
    const [charas,setCharas] = useState([])
    const [error, setError] = useState(null)
    const [loading, setLoading] = useState(true)
    
    
    useEffect(() => {
    
    const loadCharacters = async () => {
    
        try {
            const baseCharacters = await getCharacters()
            setCharas(baseCharacters['data']['characters'])
    
        } catch (err){
            console.log(err)
            setError("Failed to load character")
    
        }finally {
            setLoading(false)
        }
     }
     loadCharacters()
    
     }, [])




    function handleSearch(e){
        e.preventDefault()
        alert(searchQuery)
        setSearchQuery("")
    }


    return(

        <div className="Home">
            <form onSubmit={handleSearch} className="search-form">
                <input type="text" placeholder="Search for Characters" className="search-input" value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)}/>
                <button type="submit" className="search-bt">Search</button>
            </form>

            <div className="chara-grid">
                {charas.map((chara) => (

                  chara.name.toLowerCase().startsWith(searchQuery) && <CharacterCard chara={chara} key={chara.id}/>
                
                ))}
            </div>
        </div>

    )
}

export default Home
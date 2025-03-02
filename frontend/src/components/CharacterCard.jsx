import "../css/CharaCard.css"


function CharacterCard({chara}){

    function onFavoriteClick(){
        alert("Ola mundo")
    }


    return(
        <div className="chara-card">
            <div className="chara-image">
                <img src={chara.image} alt={chara.name}/>
            </div>

            <div className="chara-overlay">
                <button className="favorite-btn" onClick={onFavoriteClick}>❤︎‬</button>
            </div>
            <div className="chara-info">
                <h3>{chara.name}</h3>
                <p>{chara.nick}</p>
            </div>
        </div>
    )
}

export default CharacterCard
import React from 'react'
import '../App.css';


function SearchForm({query, setQuery, pagesVisited}) {
  
  const handleChange = (event) => {
    setQuery(event.target.value)
  }

  return (
    <div>
      {
        // pagesVisited !==0
        // ? null
        // : 
        <div className='search'>
          <label htmlFor='searchInputHeader'>Discover Baked Goodness </label>
          <input type="text" id="search input" onChange={handleChange} />
        </div>
      }
    </div>
  )
}

export default SearchForm
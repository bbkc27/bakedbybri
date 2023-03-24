import React from 'react';
import {useState} from 'react';
// import {Link} from 'react-paginate';
import SearchForm from './SearchForm';
// import axios from 'axios';
// import { Card } from 'react-bootstrap';

function RecipeList() {

  const [query, setQuery] = useState('');
  // const [pageNumber, setPageNumber] = useState(0)

  // const recipesPerPage= 12
  // const pagesVisited = pageNumber * recipesPerPage
  // const pageCount = Math.ceil(recipes.length / recipesPerPage)

  // const recipeListRestEndpoint = ''
  return (
    <div>

    <SearchForm query={query} setQuery={setQuery} />



    </div>
  )
}

export default RecipeList;
import React from 'react';
import {useState, useEffect} from 'react';
import {Link} from 'react-router-dom';
import axios from 'axios';
import {Card} from 'react-bootstrap'

function IngredientList(){
  
  const ingredientListEndpoint = 'http://localhost:8000/ingredients/'

  const [ingredients, setIngredients] = useState([])
  
  useEffect(() => {
    getIngredients()
  }, [])

  const getIngredients = () => {
    axios.get(ingredientListEndpoint)
    .then (res => {
      console.log(res.data)
      setIngredients(res.data)
    })
  }

  return (
    <div>

      <h3>Find Recipes by Ingredient</h3>

      <div className="ingredientCards">
        { (!ingredients)
          ? null
          : ingredients
          .map((ingredient, id) => {
            return (
              <Card className="ingredientCard" key={id} style={{width: '18rem'}}>
                <Link className="ingredientName" to={`/ingredients/${ingredient.id}`}>
                  <Card.Title>{ingredient.name}</Card.Title>
                </Link>
              </Card>
            )
          })
        }
      </div>

    </div>
  )
}

export default IngredientList;
import './App.css';
import {Routes, Route, Link} from 'react-router-dom'
import HomePage from './components/HomePage';
import {Navbar, Container} from 'react-bootstrap';
import HeaderLogo from './HeaderLogo.png';
// import SearchForm from './components/SearchForm';
import RecipeList from './components/RecipeList';
import IngredientList from './components/IngredientList';

function App() {


  return (
    <div className="App">
      
      <Navbar bg="warning" variant="success">
        <Container>
          
          <div className='topHeader'>
          <Navbar.Brand className='brand' href='/'><img className='headerLogo' src={HeaderLogo} alt="Baked By Bri Logo"/></Navbar.Brand>

            <h1 className='title'>Baked by Bri</h1>
            <Link className='menu-item' to='/recipes'>Find Recipes</Link>
          </div>


        </Container>
      </Navbar>
      <div>
        <Routes>
          <Route path='/' element={<HomePage />} />
          <Route path='/recipes' element={<RecipeList />} />
          <Route path='/ingredients' element={<IngredientList />} />
        </Routes>
      </div>

    </div>
  );
}

export default App;

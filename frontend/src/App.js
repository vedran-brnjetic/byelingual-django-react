import React from 'react';
import { Button } from 'reactstrap';
import { HeaderMenu } from './components/header_menu';


const App = () => {
	return (
	    <div>
	        <Button color="danger">ByeLingual</Button>
		<HeaderMenu />
	    </div>
	);
};

export default App;

import React from 'react';
import HeaderMenu from './components/header_menu';
import ByeCarousel from './components/bye-carousel';
import StoryContainer from './components/story_container';


const App =() => {
		return (
		    <div>
					<HeaderMenu />
					<ByeCarousel />
					<StoryContainer />
		    </div>
		);
	};

export default App;

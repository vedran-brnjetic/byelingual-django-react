import React from 'react';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  UncontrolledDropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem } from 'reactstrap';


class HeaderMenu extends React.Component {
  constructor(props) {
    super(props);

    this.toggle = this.toggle.bind(this);
    this.state = {
      isOpen: false
    };
  }
  toggle() {
    this.setState({
      isOpen: !this.state.isOpen
    });
  }
  render() {
    return (
      <div>
        <Navbar className="top-navbar" color="faded" light expand="md">
          <NavbarBrand href="/"><h3 className="navbar-title">Byelingual <span className="hidden-md-down h4">by <em>Koohii Onegai</em></span></h3></NavbarBrand>
          <NavbarToggler onClick={this.toggle} />
          <Collapse isOpen={this.state.isOpen} navbar>
            <Nav className="ml-auto" navbar>
              <NavItem>
                <NavLink href="/download/">Download</NavLink>
              </NavItem>
              <UncontrolledDropdown nav inNavbar>
                <DropdownToggle nav caret>
                  Stories
                </DropdownToggle>
                <DropdownMenu >
                  <DropdownItem>
		    <NavLink href="#story1">
                    	Cabin in the Woods
		    </NavLink>
                  </DropdownItem>
                  <DropdownItem>
		    <NavLink href="#story2">
                    	Yojijukugo
		    </NavLink>
                  </DropdownItem>
                  <DropdownItem divider />
                  <DropdownItem>
                    Bundles
                  </DropdownItem>
                </DropdownMenu>
              </UncontrolledDropdown>
              <NavItem>
                <NavLink href="/stories/">Koohii Onegai</NavLink>
              </NavItem>
              <NavItem>
                <NavLink href="https://github.com/vedran-brnjetic/Byelingual/">GitHub</NavLink>
              </NavItem>
            </Nav>
          </Collapse>

        </Navbar>
      </div>
    );
  };
}

export default HeaderMenu;

import { Link, Outlet } from 'react-router-dom'

export function Layout() {
  return (
    <div className="app-shell">
      <header className="site-header">
        <Link to="/" className="brand">
          Closeout
          <span>Field intelligence</span>
        </Link>
        <nav style={{ display: 'flex', gap: '1.25rem' }}>
          <Link className="nav-link" to="/lessons">
            Lessons
          </Link>
          <Link className="nav-link" to="/mentor">
            Mentor
          </Link>
        </nav>
      </header>
      <Outlet />
    </div>
  )
}

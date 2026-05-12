import React from 'react'

export default function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <nav className="bg-white shadow-md">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <h1 className="text-2xl font-bold text-blue-600">💰 Price Radar</h1>
        </div>
      </nav>
      
      <main className="max-w-7xl mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-xl font-semibold mb-2">Search Products</h2>
            <p className="text-gray-600">Find and compare prices across platforms</p>
          </div>
          <div className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-xl font-semibold mb-2">Price History</h2>
            <p className="text-gray-600">Track price trends over time</p>
          </div>
          <div className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-xl font-semibold mb-2">Price Alerts</h2>
            <p className="text-gray-600">Get notified on price drops</p>
          </div>
        </div>
      </main>
    </div>
  )
}

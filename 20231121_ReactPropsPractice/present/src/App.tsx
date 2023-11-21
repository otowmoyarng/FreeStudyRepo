import React from 'react';
import logo from './logo.svg';
import './App.css';
import GaveItem from "./compornent/GaveItem";
import Sabi from "./compornent/Sabi";

function App() {
  return (
    <div className="App">
      <article>
        <h1>JITTERRIN'JINN／プレゼント</h1>
        <hr />
        <GaveItem item="キリンがさかだちしたピアス" />
        <GaveItem item="フラッグチェックのハンチング" />
        <GaveItem item="ユニオンジャックのランニング" />
        <GaveItem item="丸いレンズのサングラス" />
        <GaveItem item="オレンジ色のハイヒール" />
        <GaveItem item="白い真珠のネックレス" />
        <GaveItem item="緑色した細い傘" />
        <GaveItem item="シャガールみたいな青い夜" />
        <Sabi />
      </article>
    </div>
  );
}

export default App;

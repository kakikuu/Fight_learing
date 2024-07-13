// Homeコンポーネントの作成
import React from "react";

// Homeコンポーネントの作成
const Login = () => {
  return (
    <div>
      <h1>ログイン</h1>
      <div>
        <div>
          <p>ユーザ名</p>
          <input type="text" />
        </div>
        <div>
          <p>パスワード</p>
          <input type="password" />
        </div>
      </div>
    </div>
  );
};

export default Login;

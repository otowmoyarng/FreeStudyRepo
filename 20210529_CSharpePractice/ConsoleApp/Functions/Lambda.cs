using System;
using System.Collections.Generic;
using System.Text;

namespace ConsoleApp.Functions
{
    internal class Lambda
    {
        internal void Do()
        {
            #region 戻り値のない関数を実行するラムダ式

            output("戻り値のないラムダ式を実行する");
            Action lambda1 = () => output("excute lambda noparam");
            doActionLambda(lambda1);

            Action<string> lambda2 = (msg) => output($"excute lambda param:msg->{msg}");
            doActionLambda<string>(lambda2, "hello");

            Action<string, int> lambda3 = (str, num) => output($"excute lambda param:str->{str} , num->{num}");
            doActionLambda<string, int>(lambda3, "hello", 1);

            #endregion

            #region 戻り値のある関数を実行するラムダ式

            output("戻り値があるラムダ式を実行する");
            Func<string> lambda4 = () => "lambda4";
            doFuncLambda<string>(lambda4);

            Func<int, string> lambda5 = (num) => "lambda" + Convert.ToString(num);
            doFuncLambda<int, string>(lambda5, 5);

            Func<string, int, string> lambda6 = (str, num) => str + Convert.ToString(num);
            doFuncLambda<string, int, string>(lambda6, "lambda", 6);
            #endregion

            #region ループで使用するラムダ式
            var agelist = new List<int>(new int[] { 0, 1, 2, 3, 4, 5 });
            output($"agelist -> {string.Join(',', agelist)}");

            agelist.ForEach(age => output($"agelist.ForEach age -> {age}"));
            
            agelist.Sort((age1, age2) => age2 - age1);
            output($"agelist desc -> {string.Join(',', agelist)}");
            
            agelist.Sort((age1, age2) => age1 - age2);
            output($"agelist asc -> {string.Join(',', agelist)}");

            bool isexist = agelist.Exists(age => age == 2);
            output($"agelist.Exists(age == 2) return -> {isexist}");

            isexist = agelist.Exists(age => age == 10);
            output($"agelist.Exists(age == 10) return -> {isexist}");
            #endregion
        }

        private void output(string value)
        {
            Console.WriteLine(value);
        }

        private void doActionLambda(Action lambda)
        {
            lambda();
        }

        private void doActionLambda<T>(Action<T> lambda, T msg)
        {
            lambda(msg);
        }

        private void doActionLambda<T1, T2>(Action<T1, T2> lambda, T1 param1, T2 param2)
        {
            lambda(param1, param2);
        }

        private void doFuncLambda<TResult>(Func<TResult> lambda)
        {
            TResult result = lambda();
            output($"excute lambda noparam return -> {result.ToString()}");
        }
        private void doFuncLambda<T1, TResult>(Func<T1, TResult> lambda, T1 param1)
        {
            TResult result = lambda(param1);
            output($"excute lambda param1->{param1}, return -> {result.ToString()}");
        }
        private void doFuncLambda<T1, T2, TResult>(Func<T1, T2, TResult> lambda, T1 param1, T2 param2)
        {
            TResult result = lambda(param1, param2);
            output($"excute lambda param1->{param1}, param2->{param2}, return -> {result.ToString()}");
        }
    }
}

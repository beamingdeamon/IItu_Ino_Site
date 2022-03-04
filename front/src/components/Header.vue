<template>
    <div class="wrapper">
        <div class="front">
            <div class="left-header-content">
                <div class="nav_button">
                    <div class="nav_click" @click="nav_open">
                        <span> {{ this.currentBlock }} </span>
                    </div>
                    <nav class="menu">
                        <a href="#sec1">1</a>
                        <a href="#sec2">2</a>
                        <a href="#sec3">3</a>
                        <a href="#sec4">4</a>
                        <a href="#sec5">5</a>
                        <a href="#sec6">6</a>
                    </nav>
                </div>
                
                <div class="logo"> <router-link to="/"></router-link></div>
                <div class="logo-1"> <router-link to="/"></router-link></div>
                <div class="logo-2"> <router-link to="/"></router-link></div>
            </div>
            <div class="center-header-content">
                <div class="logo"> <router-link to="/"></router-link></div>
                <div class="logo-1"> <router-link to="/"></router-link></div>
                <div class="logo-2"> <router-link to="/"></router-link></div>
                <nav>
                    <ul>
                        <li>
                            <a href="#sec2">Бағдарлама</a>
                        </li>
                        <li>
                            <a href="#sec3">Не үйренесің?</a>
                        </li>
                        <li>
                            <a href="#sec4">Курс сен үшін</a>
                        </li>
                        <li>
                            <a href="#sec5">Бонустар</a>
                        </li>
                        <li>
                            <a href="#sec6">Курс авторы</a>
                        </li>
                        <li>
                            <a href="#sec7">Төлем</a>
                        </li>
                    </ul>
                </nav>
            </div>
            
                <div class="call-center">
                    <a href="https://api.whatsapp.com/send?phone=+77771456152"></a>
                </div>
            </div>
        </div>
</template>

<script>
const $ = require( "jquery" )
export default {
    name: 'Header',
    data: () => ({
    }),
    methods:{
        mob_menu(){
            $('.prof_modal').sass({'display': 'block'})
        },
        nav_open() {
            $('nav.menu').toggleClass('menu_active')
        }
    }
}
</script>

<style lang="sass" scoped>
    @font-face
        font-family: GothamLight
        src: url(../assets/Gotham/GothamLight.ttf)
    @font-face
        font-family: SuitcaseTypeFoundryAtypRegularVariable
        src: url(../assets/AtypRegularVariable/SuitcaseTypeFoundryAtypRegularVariable.ttf)
    .mobileMenu
        width: 55px !important
        height: 100% !important
        margin-left: 5%
        display: flex
        align-items: center
        justify-content: center
        cursor: pointer
        display: none
        z-index: 100
        .buble
            width: 70% !important
            height: 2px !important
            background-color: #FA1451
            position: relative
            z-index: 100
            &:before, &:after
                content: ''
                width: 7.5vw !important
                height: 2px !important
                background-color: #FA1451
                position: absolute
                z-index: 100
            &:before
                top: -500%
            &:after
                bottom: -500%
        
    .wrapper
        width: 100vw
        height: 67px
        background-color: #000
        position: fixed
        left: 0
        top: 0
        background-color: #3D3D3D
        z-index: 200
        .front
            max-width: 1440px
            height: 100%
            margin: 0 auto
            color: white
            display: flex
            justify-content: space-between
            align-items: center
            .left-header-content
                width: 25%
                height: 100%
                display: flex
                .nav_button
                    display: none
                    width: 58px
                    height: 58px
                    border-radius: 50%
                    border: 1px solid #FFFFFF
                    justify-content: center
                    align-items: center
                    position: relative
                    background-color: #3D3D3D
                    
                    .nav_click
                        cursor: pointer
                        span
                            position: absolute
                            left: 50%
                            top: 50%
                            transform: translate(-50%, -50%)
                            color: white
                            font-size: 6vw
                            z-index: 201
                    .menu
                        a
                            display: flex
                            justify-content: center
                            align-items: center
                            width: 58px
                            height: 58px
                            border-radius: 50%
                            border: 1px solid #fff
                            color: white
                            text-decoration: none
                            font-size: 6vw
                            transition: .6s
                            position: absolute
                            left: 50%
                            top: 50%
                            transform: translate(-50%, -50%)
                            z-index: -1
                    .menu_active a:nth-child(1)
                        transform: translate(-50%, 100%)
                    .menu_active a:nth-child(2)
                        transform: translate(-50%, 230%)
                    .menu_active a:nth-child(3)
                        transform: translate(-50%, 360%)
                    .menu_active a:nth-child(4)
                        transform: translate(-50%, 490%)
                    .menu_active a:nth-child(5)
                        transform: translate(-50%, 620%)
                    .menu_active a:nth-child(6)
                        transform: translate(-50%, 750%)
                    .menu_active a:nth-child(7)
                        transform: translate(-50%, 880%)
                    .menu_active a:nth-child(8)
                        transform: translate(-50%, 1010%)
                    
            .right-header-content
                width: 20% !important
                height: 100%
                display: flex
                justify-content: space-around
                align-items: center
                .mobile-account
                    width: 58px
                    height: 58px
                    justify-content: center
                    align-items: center
                    border-radius: 50%
                    border: 1px solid #ffffff
                    display: none
                    position: relative
                    a
                        position: absolute
                        width: 100%
                        height: 100%
                .call-center
                    background: url(../assets/phone.svg) center no-repeat
                    background-size: contain
                    cursor: pointer
                    position: relative
                    width: 100%
                    height: 60%
                    a
                        width: 100%
                        height: 100%
                        display: block
                    .account-fixed-register
                        width: 3.8vw
                        height: 3.8vw
                        position: absolute
                        right: 0vw
                        top: 8vh
                        border-radius: 50%
                        border: 1px solid #FFF
                        background: #3D3D3D url(../assets/user1.svg) center no-repeat
                        background-size: 45%
                        animation: radial-pulse 1s infinite
                        transition: .5s
                        a
                            width: 100%
                            height: 100%
                            display: block
                        &:hover
                            transform: scale(1.15)
                    .account-fixed-autorized
                        width: 3.8vw
                        height: 3.8vw
                        position: absolute
                        right: 10vw
                        top: 8vh
                        border-radius: 50%
                        border: 1px solid #FFF
                        background: #3D3D3D url(../assets/user1.svg) center no-repeat
                        background-size: 45%
                        animation: radial-pulse 1s infinite
                        transition: .5s
                        display: block
                        .passed
                            position: relative
                            width: 100%
                            height: 100%
                            .autorized
                                width: 400%
                                height: 100%
                                display: flex
                                position: absolute
                                right: -400%
                                bottom: 0
                                justify-content: flex-start
                                align-items: center
                                font-size: 2.1vh
                                white-space: nowrap
                                text-transform: capitalize
                                color: white
                                font-family: GothamLight
                                text-align: left
                                padding-left: 20%
                                line-height: 2.5vh
                                    
                        &:hover
                            transform: scale(1.15)
                    ul
                        display: none
                        flex-direction: column
                        justify-content: space-evenly
                        align-items: center
                        background-color: #3D3D3D
                        width: 13vw
                        height: 15vh
                        position: absolute
                        bottom: -500%
                        left: 0
                        z-index: 100
                        &:hover
                            display: flex
                        &:first-child
                            color: #FA1451
                            font-family: GothamLight
                        li
                            width: 100%
                            text-align: center
                            font-size: 1.5vh
                            a
                                color: white
                                text-decoration: none
                            span
                                background: url(../assets/phone.svg) center no-repeat
                                background-size: 30%
                                display: inline-block
            .logo, .logo-1, .logo-2
                height: 100%
                cursor: pointer
                a
                    width: 100%
                    height: 100%
                    display: block
            .logo
                background: url(../assets/Comp6_000001.svg) center no-repeat
                width: 33%
            .logo-1
                background: url(../assets/UDB.svg) center no-repeat
                background-size: contain
                background-position-x: center
                background-position-y: 60%
                width: 35%
            .logo-2
                background: url(../assets/onlineschool.svg) center no-repeat
                background-size: contain
                width: 31%
                margin-left: 3%
            .center-header-content
                min-width: 80%
                height: 100%
                .logo, .logo-1, .logo-2
                    display: none
                nav
                    min-width: 100%
                    height: 100%
                    display: flex
                    align-items: center
                    font-size: 1.7vh
                    line-height: 28px
                    margin: 0 auto
                    color: #FFFFFF
                    
                    ul
                        display: flex
                        justify-content: space-evenly
                        width: 100%
                        a
                            color: white
                            text-decoration: none
                            font-size: 1.3em
                            font-family: SuitcaseTypeFoundryAtypRegularVariable
                            position: relative
                            
                            &:before
                                content: ''
                                position: absolute
                                left: 0
                                bottom: 0
                                width: 0%
                                height: 1px
                                background-color: white
                                transition: .5s
                            &:hover:before
                                width: 100%
                            &:hover
                                color: rgb(245, 0, 65)
    @keyframes radial-pulse
        0%
            box-shadow: 0 0 0 0px rgba(0, 0, 0, 0.5)
        100%
            box-shadow: 0 0 0 40px rgba(0, 0, 0, 0)
    @media (max-width: 1024px)
        .center-header-content
            min-width: 60% !important
            display: flex
            justify-content: center
            align-items: center
            .logo, .logo-1, .logo-2, 
                display: block 
                width: 25% !important
            nav
                display: none 
        .left-header-content
            display: flex
            justify-content: center
            align-items: center
            .logo, .logo-1, .logo-2, 
                display: none 
            .nav_button
                display: block 
        .right-header-content
            .call-center
                display: none 
            .mobile-account
                display: flex 
</style>
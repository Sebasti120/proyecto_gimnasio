/* =====================================================
   SENA Gym — Layout compartido (inyectado por JS)
   Cada página llama a SENA.initLayout({ active: '...', breadcrumb: '...' })
   y este script inyecta sidebar + topbar + backdrop automáticamente.
   ===================================================== */

(function () {
    'use strict';

    const NAV_ITEMS = [
        { type: 'section', label: 'Principal' },
        { href: '../index.html',   icon: 'bi-grid-1x2-fill',     label: 'Dashboard',     id: 'dashboard' },
        { href: 'rutinas.html',    icon: 'bi-clipboard2-pulse',  label: 'Rutinas',       id: 'rutinas' },
        { href: 'ejercicios.html', icon: 'bi-activity',          label: 'Ejercicios',    id: 'ejercicios' },
        { href: 'entrenamientos.html', icon: 'bi-stopwatch',     label: 'Entrenamientos', id: 'entrenamientos' },

        { type: 'section', label: 'Recursos' },
        { href: 'equipos.html',    icon: 'bi-tools',             label: 'Equipos',         id: 'equipos',   badge: '75' },
        { href: 'mantenimiento.html', icon: 'bi-wrench-adjustable-circle-fill', label: 'Mantenimiento', id: 'mantenimiento', badge: '4' },
        { href: 'espacios.html',   icon: 'bi-geo-alt-fill',      label: 'Espacios',        id: 'espacios' },
        { href: 'inventario.html', icon: 'bi-box-seam',          label: 'Inventario',      id: 'inventario' },

        { type: 'section', label: 'Personas' },
        { href: 'usuarios.html',   icon: 'bi-people-fill',       label: 'Usuarios',        id: 'usuarios',  badge: '320' },
        { href: 'ingresos.html',   icon: 'bi-fingerprint',       label: 'Control de ingreso', id: 'ingresos' },
        { href: 'valoracion.html', icon: 'bi-heart-pulse-fill',  label: 'Valoración física', id: 'valoracion' },

        { type: 'section', label: 'Sistema' },
        { href: 'informacion.html', icon: 'bi-info-circle-fill', label: 'Información',    id: 'informacion' }
    ];

    function escapeHtml(s) {
        return String(s).replace(/[&<>"']/g, m => ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[m]));
    }

    function buildSidebar(activeId, navItems) {
        navItems = navItems || NAV_ITEMS;
        let navHtml = '';
        navItems.forEach(item => {
            if (item.type === 'section') {
                navHtml += '<div class="sidebar-section-title">' + escapeHtml(item.label) + '</div>';
            } else {
                const isActive = item.id === activeId ? ' active' : '';
                const badgeHtml = item.badge ? '<span class="badge">' + escapeHtml(item.badge) + '</span>' : '';
                navHtml += '<a href="' + item.href + '" class="sidebar-link' + isActive + '" data-id="' + item.id + '" data-label="' + escapeHtml(item.label) + '">' +
                    '<i class="bi ' + item.icon + '"></i>' +
                    '<span class="label">' + escapeHtml(item.label) + '</span>' +
                    badgeHtml +
                '</a>';
            }
        });

        return '' +
        '<aside class="app-sidebar" aria-label="Navegación principal">' +
            '<div class="sidebar-brand">' +
                '<div class="sidebar-brand-logo">S</div>' +
                '<div class="sidebar-brand-text">' +
                    '<span class="sidebar-brand-name">SENA Gym</span>' +
                    '<span class="sidebar-brand-sub">Gestión interna</span>' +
                '</div>' +
            '</div>' +
            '<nav class="sidebar-nav">' + navHtml + '</nav>' +
            '<div class="sidebar-footer">' +
                '<div class="sidebar-user" title="Sesión activa">' +
                    '<div class="user-avatar">JS</div>' +
                    '<div class="user-info">' +
                        '<div class="user-name">Juan Salgado</div>' +
                        '<div class="user-role">Administrador · SENA</div>' +
                    '</div>' +
                '</div>' +
            '</div>' +
        '</aside>' +
        '<div class="sidebar-backdrop" aria-hidden="true"></div>';
    }

    function buildTopbar(activeId, navItems) {
        navItems = navItems || NAV_ITEMS;
        const currentItem = navItems.find(i => i.id === activeId);
        const pageTitle = currentItem ? currentItem.label : 'Dashboard';
        return '' +
        '<header class="app-topbar">' +
            '<button class="topbar-toggle" data-action="toggle-sidebar" aria-label="Alternar menú lateral">' +
                '<i class="bi bi-list"></i>' +
            '</button>' +
            '<div class="topbar-breadcrumb" data-breadcrumb></div>' +
            '<div class="topbar-search">' +
                '<i class="bi bi-search"></i>' +
                '<input type="search" placeholder="Buscar en el sistema..." aria-label="Buscar">' +
            '</div>' +
            '<div class="topbar-actions">' +
                '<button class="topbar-icon-btn" title="Notificaciones" aria-label="Notificaciones">' +
                    '<i class="bi bi-bell"></i>' +
                    '<span class="dot"></span>' +
                '</button>' +
                '<button class="topbar-icon-btn" title="Ayuda" aria-label="Ayuda">' +
                    '<i class="bi bi-question-circle"></i>' +
                '</button>' +
            '</div>' +
        '</header>';
    }

    /**
     * Inicializa el layout compartido.
     * Llamar en cada página antes del cierre del body.
     *
     * @param {Object} opts
     * @param {string} opts.active   - id del item activo (coincide con NAV_ITEMS[i].id)
     * @param {string} opts.title    - título H1 de la página (opcional, default = label del item)
     * @param {string} opts.subtitle - subtítulo del page header
     * @param {boolean} opts.inRoot  - true si la página vive en la raíz del proyecto (index.html)
     *                                 En ese caso los href se prefijan con "pages/".
     *                                 Default: false (página dentro de /pages).
     */
    window.SENA = window.SENA || {};
    window.SENA.initLayout = function (opts) {
        opts = opts || {};
        const activeId = opts.active || 'dashboard';
        const prefix = opts.inRoot ? 'pages/' : '';

        // Re-escribir NAV_ITEMS con prefijo según contexto
        const navItems = NAV_ITEMS.map(item => {
            if (item.type === 'section') return item;
            return Object.assign({}, item, { href: prefix + item.href });
        });

        const sidebarHost = document.getElementById('app-sidebar-host');
        const topbarHost  = document.getElementById('app-topbar-host');

        if (sidebarHost) sidebarHost.outerHTML = buildSidebar(activeId, navItems);
        if (topbarHost)  topbarHost.outerHTML  = buildTopbar(activeId, navItems);

        const titleEl = document.getElementById('page-title');
        const subtitleEl = document.getElementById('page-subtitle');
        if (titleEl) {
            const item = navItems.find(i => i.id === activeId);
            titleEl.textContent = opts.title || (item ? item.label : 'Dashboard');
        }
        if (subtitleEl && opts.subtitle) subtitleEl.textContent = opts.subtitle;
    };
})();

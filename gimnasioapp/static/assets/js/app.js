/* =====================================================
   SENA Gym — JS compartido de la aplicación
   Sidebar, topbar, helpers, persistencia ligera
   ===================================================== */

(function () {
    'use strict';

    /* ====== Estado persistido (localStorage) ====== */
    const STORAGE_KEY = 'senagym_prefs';
    const getPrefs = () => {
        try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {}; }
        catch (e) { return {}; }
    };
    const setPrefs = (prefs) => {
        try { localStorage.setItem(STORAGE_KEY, JSON.stringify(prefs)); } catch (e) {}
    };

    /* ====== Sidebar: colapsar/expandir (desktop) ====== */
    function initSidebar() {
        const sidebar = document.querySelector('.app-sidebar');
        if (!sidebar) return;

        const prefs = getPrefs();
        if (prefs.sidebarCollapsed && window.innerWidth >= 768) {
            document.body.classList.add('sidebar-collapsed');
            sidebar.classList.add('collapsed');
        }

        const toggleBtn = document.querySelector('[data-action="toggle-sidebar"]');
        if (toggleBtn) {
            toggleBtn.addEventListener('click', () => {
                if (window.innerWidth < 768) {
                    sidebar.classList.toggle('mobile-open');
                    document.querySelector('.sidebar-backdrop')?.classList.toggle('visible');
                } else {
                    document.body.classList.toggle('sidebar-collapsed');
                    sidebar.classList.toggle('collapsed');
                    setPrefs({ ...getPrefs(), sidebarCollapsed: sidebar.classList.contains('collapsed') });
                }
            });
        }

        const backdrop = document.querySelector('.sidebar-backdrop');
        if (backdrop) {
            backdrop.addEventListener('click', () => {
                sidebar.classList.remove('mobile-open');
                backdrop.classList.remove('visible');
            });
        }
    }

    /* ====== Marcar link activo en sidebar ====== */
    function highlightActiveLink() {
        const currentPath = window.location.pathname.split('/').pop() || 'index.html';
        document.querySelectorAll('.sidebar-link').forEach(link => {
            const href = link.getAttribute('href');
            if (!href || href.startsWith('#')) return;
            const linkFile = href.split('/').pop();
            if (linkFile === currentPath) {
                link.classList.add('active');
            }
        });
    }

    /* ====== Breadcrumb automático ====== */
    function renderBreadcrumb() {
        const bc = document.querySelector('[data-breadcrumb]');
        if (!bc) return;
        const currentLink = document.querySelector('.sidebar-link.active');
        const moduleLabel = currentLink ? currentLink.dataset.label || currentLink.querySelector('.label')?.textContent.trim() : 'Inicio';
        const segs = ['<strong id="bc-current">' + escapeHtml(moduleLabel) + '</strong>'];
        bc.innerHTML = '<span>Inicio</span><span class="separator">/</span>' + segs.join('<span class="separator">/</span>');
    }

    function escapeHtml(s) {
        return String(s).replace(/[&<>"']/g, m => ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[m]));
    }

    /* ====== Toast helper ====== */
    window.showToast = function (message, opts = {}) {
        const existing = document.querySelector('.toast-app');
        if (existing) existing.remove();
        const toast = document.createElement('div');
        toast.className = 'toast-app';
        toast.innerHTML = '<i class="bi ' + (opts.icon || 'bi-check-circle-fill') + '"></i><span>' + escapeHtml(message) + '</span>';
        document.body.appendChild(toast);
        requestAnimationFrame(() => toast.classList.add('visible'));
        setTimeout(() => {
            toast.classList.remove('visible');
            setTimeout(() => toast.remove(), 250);
        }, opts.duration || 2800);
    };

    /* ====== Filtro genérico de tabla ====== */
    window.bindTableFilter = function (inputSelector, tableSelector) {
        const input = document.querySelector(inputSelector);
        const table = document.querySelector(tableSelector);
        if (!input || !table) return;
        input.addEventListener('input', () => {
            const q = input.value.trim().toLowerCase();
            table.querySelectorAll('tbody tr').forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = !q || text.includes(q) ? '' : 'none';
            });
        });
    };

    /* ====== Confirma acción ====== */
    window.confirmAction = function (message) {
        return window.confirm(message);
    };

    /* ====== INIT ====== */
    document.addEventListener('DOMContentLoaded', () => {
        initSidebar();
        highlightActiveLink();
        renderBreadcrumb();
    });
})();
